import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

from ..serializers import CreateSimulationSerializer
from .api_requests import *
from .mouse import Mouse
import time
import threading

class SimulationConsumer(WebsocketConsumer):

    def connect(self):
        self.lab_name = self.scope['url_route']['kwargs']['lab_name']
        self.lab_group_name = f'simulation_{self.lab_name}'

        self.accept()

        async_to_sync(self.channel_layer.group_add)(
            self.lab_group_name,
            self.channel_name,
        )
    
    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(
            self.lab_group_name,
            self.channel_name,
        )
    
    def receive(self, text_data=None, bytes_data=None):
        try:
            text_data_json = json.loads(text_data)
        except ValueError:
            self.send_error_msg("Cannot convert payload to json")

        
        serializer = CreateSimulationSerializer(data=text_data_json)

        if not serializer.is_valid():
            self.send_error_msg("Simulation payload is wrong")
        
        payload = serializer.data

        self.create_simulation(payload)

        # async_to_sync(self.channel_layer.group_send)(
        #     self.lab_group_name,
        #     {
        #         "type": "create_simulation",
        #         "payload": payload,
        #     },
        # )
    
    def send_error_msg(self, msg):
        self.send(text_data=json.dumps(
            {
                "type": "error",
                "message": msg
            }
        ))
    
    def send_info_msg(self, msg):
        self.send(text_data=json.dumps(
            {
                "type": "info",
                "message": msg
            }
        ))

    def send_mouse_status(self, mouse):
        self.send(
            text_data=json.dumps(
                {
                    "type": "mouse_status",
                    "mouse": {
                        "id": mouse.id,
                        "intelligence": mouse.intelligence,
                        "health": mouse.health,
                        "mental": mouse.mental,
                        "current_room": mouse.current_room.get("room_number")
                    }
                }
            )
        )

    def create_simulation(self, payload):
        self.send_info_msg("Creating Simulation")

        labyrinth_id = payload.get("labyrinth_id")
        rule_set_id = payload.get("ruleSet_id")
        mouses_intelligences = payload.get("mouses_intelligence")

        self.send_info_msg("Retrieving labyrinth")
        labyrinth = get_labyrinth(labyrinth_id)
        
        self.send_info_msg("Retrieving intelligences")
        intelligences = get_intelligences()

        self.send_info_msg("Retrieving action rules")
        action_rules = get_action_rule_for_rule_set(rule_set_id)

        self.send_info_msg("Retrieving objective rules")
        objective_rules = get_objective_rule_for_rule_set(rule_set_id)

        self.send_info_msg("Generating Mouses")
        mouses = []
        mouse_id = 0
        for mouse_i in mouses_intelligences :
            print("mouse_i", mouse_i)
            intelligence_id = mouse_i.get("intelligence_id")
            number_of_mouses = mouse_i.get("number_of_mouses")
            for i in range(number_of_mouses):
                print("m", i)
                mouse_id = mouse_id + 1
                print("mouse_id", mouse_id)
                for i in intelligences :
                    if i.get("id") == intelligence_id:
                        intelligence_level = i.get("max_level")
                        mouse = Mouse(mouse_id, intelligence_level, 10, 10, None)
                        mouses.append(mouse)
        print("number of mouses", mouses)
        self.assign_intelligences(mouses, labyrinth, action_rules, objective_rules)



    def assign_intelligences(self, mouses, labyrinth, action_rules, objective_rules):
        self.send_info_msg("Assigning intelligences to mouses")
        
        lab_entrance = labyrinth[0]
        
        for mouse in mouses: 
            if mouse.intelligence >= 7:
                self.send_info_msg(f"Assigning DFS to mouse {mouse.id}")
                
                visited_dfs = []
                parents = [lab_entrance]

                th_dfs = threading.Thread(
                    target=self.dfs_intelligence,
                    args=(
                visited_dfs, 
                labyrinth, 
                lab_entrance, 
                lab_entrance, 
                parents, 
                False,
                mouse, 
                action_rules, 
                objective_rules
                ))
                th_dfs.start()
                # self.dfs_intelligence(
                # visited=visited_dfs, 
                # labyrinth=labyrinth, 
                # room=lab_entrance, 
                # parent=lab_entrance, 
                # parents=parents, 
                # exit_found=False,
                # mouse=mouse, 
                # action_rules=action_rules, 
                # objective_rules=objective_rules
                # )
            
            elif mouse.intelligence >= 4 : 
                self.send_info_msg(f"Assigning BFS to mouse {mouse.id}")
                visited_bfs = []
                queue_bfs = []
                
                th_bfs = threading.Thread(
                    target=self.bfs_intelligence,
                    args=(visited_bfs, labyrinth, lab_entrance, queue_bfs, mouse, action_rules, objective_rules))
                th_bfs.start()
                # self.bfs_intelligence(visited_bfs, labyrinth, lab_entrance, queue_bfs, mouse, action_rules, objective_rules)
            
            elif mouse.intelligence > 10:
                self.send_info_msg(f"Mouse {mouse.id} is cheating")
                route = self.bfs_intelligence_cheating_mouse(self, labyrinth, lab_entrance, mouse, action_rules, objective_rules)
                th_cheating = threading.Thread(
                    target=self.handle_cheating_mouse_route,
                    args=(
                        route,
                        mouse,
                        action_rules,
                        objective_rules
                        ))
                th_cheating.start()
                # self.handle_cheating_mouse_route(route, mouse, action_rules, objective_rules)


    def dfs_intelligence(self, visited, labyrinth, room, parent, parents, exit_found, mouse, action_rules, objective_rules):
        if (room.get("room_number") not in visited):
            parents.append(parent)
            
            self.ask_mouth_to_take_a_step( mouse, visited, room, action_rules, objective_rules)

            if room.get("is_lab_exit"):
                # print("Mouse has reached the exit")
                exit_found = True
                return exit_found
            else:
                available_exits_ids = room.get("available_exits")
                # print (f"Available Exists are {available_exits_ids}")
                available_exits = self.get_room_from_number(available_exits_ids, labyrinth)
        
                #Si la souris est dans une impasse il faut noter qu'elle est revenue en arriere
                if len(available_exits_ids) == 1 and available_exits_ids[0] in visited:
                    # print("Mouse hit a wall... backtracking...")
                    next_room = self.dfs_backtrack(visited, labyrinth, parents, mouse, action_rules, objective_rules)
                    if next_room and not exit_found: 
                        exit_found = self.dfs_intelligence(visited, labyrinth, next_room, room, parents, exit_found, mouse, action_rules, objective_rules)
                    return exit_found
                else: 
                    for next_room in available_exits:
                        if not exit_found:
                            node = next_room.get("room_number")
                            # print("Mouse is visiting next node", node)
                            exit_found = self.dfs_intelligence(visited, labyrinth, next_room, room, parents, exit_found, mouse, action_rules, objective_rules)
                    return exit_found
        return exit_found
    
    def dfs_backtrack(self, visited, labyrinth, parents, mouse, action_rules, objective_rules): 
        current_parent = parents.pop()

        self.ask_mouth_to_take_a_step(mouse, visited, current_parent, action_rules, objective_rules)

        parent_room_number = current_parent.get("room_number")
        # print (f"Mouse backtracked to {parent_room_number}")
    
        available_exits_ids = current_parent.get("available_exits")
        # print (f"Parents Available Exists are {available_exits_ids}")

        last_n_rooms = visited[-40:]
        # print (f"last_n_rooms {last_n_rooms}")

        exit_rooms_visited = all(rooms in last_n_rooms for rooms in available_exits_ids)
        if exit_rooms_visited:
            # print("Backtracking again. The mouse already visited all nodes")
            self.dfs_backtrack(visited, labyrinth, parents, mouse, action_rules, objective_rules)
        else:
            # print("Mouse found an unvisited room... going there")
            available_exits = self.get_room_from_number(available_exits_ids, labyrinth)
            for next_room in available_exits:
                if next_room.get("room_number") not in visited:
                    # print("Unvisited room is", next_room.get("room_number") )
                    return next_room
                
    def bfs_intelligence(self, visited, labyrinth, room, queue, mouse, action_rules, objective_rules): 
        queue.append(room)
        exit_found = False
    
        while (queue and not exit_found):     
            current_room = queue.pop(0) 
            # print (current_room, end = " ") 
        
            available_exits_ids = current_room.get("available_exits")
            # print (f"Available Exists are {available_exits_ids}")
            available_exits = self.get_room_from_number(available_exits_ids, labyrinth)
        
            #On retrace le chemin pour aller visiter les autres noeud 
            if visited:
                self.bfs_backtracking(mouse, visited, current_room.get("room_number"), action_rules, objective_rules, labyrinth)

            for next_room in available_exits:
                # print("Next Room is ", next_room.get("room_number"))
                if next_room.get("room_number") not in visited:
                    self.ask_mouth_to_take_a_step(mouse, visited, current_room, action_rules, objective_rules)
                    self.ask_mouth_to_take_a_step(mouse, visited, next_room, action_rules, objective_rules)
                    # visited.append(current_room.get("room_number"))
                    # visited.append(next_room.get("room_number"))
                    queue.append(next_room)
                
                    if next_room.get("is_lab_exit"):
                        exit_found = True
                        # print("Mouse has reached the exit")
                        break
    
    def bfs_backtracking(self,mouse, visited, backtrack_to_room, action_rules, objective_rules, labyrinth):
        path = visited
        last_element = visited[-1]

        for room in reversed(path):
            if room == backtrack_to_room:
                return visited
            elif room == last_element:
                continue
            else:
                # visited.append(room)
                ret = self.get_room_from_number([room], labyrinth)
                self.ask_mouth_to_take_a_step(mouse, visited, ret.pop(), action_rules, objective_rules)

    def bfs_intelligence_cheating_mouse(self, labyrinth, room, action_rules, objective_rules):
        queue = []
        queue.append([room])
    
        visited = []
        visited.append(room.get("room_number"))

        while queue:
            path = queue.pop(0) 
            current_room = path[-1]
            if current_room.get("is_lab_exit"):
                return path
        

            available_exits_ids = current_room.get("available_exits")
            # print (f"Available Exists are {available_exits_ids}")
            available_exits = self.get_room_from_number(available_exits_ids, labyrinth)

            for next_room in available_exits:
                if next_room.get("room_number") not in visited:
                    visited.append(next_room.get("room_number"))
                    new_path = list(path)
                    new_path.append(next_room)
                    queue.append(new_path)
    
    def get_room_from_number(self, rom_numbers, labyrinth):
        rooms = []
        for room in labyrinth:
            if room.get("room_number") in rom_numbers:
                rooms.append(room)
        return rooms
    
    def ask_mouth_to_take_a_step(self, mouse, visited, room, action_rules, objective_rules ):
        mouse.take_step(room, action_rules, objective_rules)
        visited.append(room.get("room_number"))
        self.send_mouse_status(mouse)
        time.sleep(1)

    def handle_cheating_mouse_route(self,route, mouse, action_rules, objective_rules):
        for room in route:
            self.ask_mouth_to_take_a_step(self, mouse, [], room, action_rules, objective_rules )