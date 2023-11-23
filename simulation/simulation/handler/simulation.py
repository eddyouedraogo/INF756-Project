from .api_requests import *


def create_simulation(payload):
    print("******** Creating Simulation ******")
    labyrinth_id = payload.get("labyrinth_id")
    rule_set_id = payload.get("ruleSet_id")


    labyrinth = get_labyrinth(labyrinth_id)
    intelligences = get_intelligences()
    action_rules = get_action_rule_for_rule_set(rule_set_id)
    objective_rules = get_objective_rule_for_rule_set(rule_set_id)

    
    visited_dfs = []
    queue_bfs = []
    visited_bfs = []
    visited_dfs_smart_mouse = []
    visited_bfs_smart_mouse = []
    queue_bfs_smart_mouse = []

    lab_entrance = labyrinth[0]
    parents = [lab_entrance]
    
    dfs_intelligence(
        visited=visited_dfs, 
        labyrinth=labyrinth, 
        room=lab_entrance, 
        parent=lab_entrance, 
        parents=parents, 
        exit_found=False
        )
    
    bfs_intelligence(visited_bfs, labyrinth, lab_entrance, queue_bfs)

    route = bfs_intelligence_smart_mouse(labyrinth, lab_entrance)
    path = [room.get("room_number") for room in route]

    return {
        "visited_dfs": visited_dfs,
        "visited_bfs": visited_bfs,
        "visited_dfs_smart_mouse": visited_dfs_smart_mouse,
        "visited_bfs_smart_mouse": path,
        }

def dfs_intelligence(visited, labyrinth, room, parent, parents, exit_found):
    print("***************************** BEGINNING DFS ************************")

    if (room.get("room_number") not in visited):
        parents.append(parent)
        print ("The mouse is currently in room ", room.get("room_number"))
        visited.append(room.get("room_number"))

        if room.get("is_lab_exit"):
            print("Mouse has reached the exit")
            exit_found = True
            return exit_found
        else:
            available_exits_ids = room.get("available_exits")
            print (f"Available Exists are {available_exits_ids}")
            available_exits = get_room_from_number(available_exits_ids, labyrinth)
        
            #Si la souris est dans une impasse il faut noter qu'elle est revenue en arriere
            if len(available_exits_ids) == 1 and available_exits_ids[0] in visited:
                print("Mouse hit a wall... backtracking...")
                next_room = dfs_backtrack(visited, labyrinth, parents)
                if next_room and not exit_found: 
                    exit_found = dfs_intelligence(visited, labyrinth, next_room, room, parents, exit_found)
                return exit_found
            else: 
                for next_room in available_exits:
                    if not exit_found:
                        node = next_room.get("room_number")
                        print("Mouse is visiting next node", node)
                        exit_found = dfs_intelligence(visited, labyrinth, next_room, room, parents, exit_found)
                return exit_found
    return exit_found

def dfs_backtrack(visited, labyrinth, parents): 
    current_parent = parents.pop()

    visited.append(current_parent.get("room_number"))
    parent_room_number = current_parent.get("room_number")
    print (f"Mouse backtracked to {parent_room_number}")
    
    available_exits_ids = current_parent.get("available_exits")
    print (f"Parents Available Exists are {available_exits_ids}")

    last_n_rooms = visited[-40:]
    print (f"last_n_rooms {last_n_rooms}")

    exit_rooms_visited = all(rooms in last_n_rooms for rooms in available_exits_ids)
    if exit_rooms_visited:
        print("Backtracking again. The mouse already visited all nodes")
        dfs_backtrack(visited, labyrinth, parents)
    else:
        print("Mouse found an unvisited room... going there")
        available_exits = get_room_from_number(available_exits_ids, labyrinth)
        for next_room in available_exits:
            if next_room.get("room_number") not in visited:
                print("Unvisited room is", next_room.get("room_number") )
                return next_room

# def dfs_backtrack(visited, labyrinth, parents): 

#     for room in reversed(parents):
#         visited.append(room.get("room_number"))
#         if room.get("available_exits") not in visited:
#             return room

def bfs_intelligence(visited, labyrinth, room, queue): 
    queue.append(room)
    exit_found = False
    
    while (queue and not exit_found):     
        current_room = queue.pop(0) 
        print (current_room, end = " ") 
        
        available_exits_ids = current_room.get("available_exits")
        print (f"Available Exists are {available_exits_ids}")
        available_exits = get_room_from_number(available_exits_ids, labyrinth)
        
        #On retrace le chemin pour aller visiter les autres noeud 
        if visited:
            bfs_backtracking(visited, current_room.get("room_number"))

        for next_room in available_exits:
            print("Next Room is ", next_room.get("room_number"))
            if next_room.get("room_number") not in visited:
                visited.append(current_room.get("room_number"))
                visited.append(next_room.get("room_number"))
                queue.append(next_room)
                
                if next_room.get("is_lab_exit"):
                    exit_found = True
                    print("Mouse has reached the exit")
                    break

def bfs_backtracking(visited, backtrack_to_room):
    path = visited
    last_element = visited[-1]

    for room in reversed(path):
        if room == backtrack_to_room:
            return visited
        elif room == last_element:
            continue
        else:
            visited.append(room)

def bfs_intelligence_smart_mouse(labyrinth, room):
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
        print (f"Available Exists are {available_exits_ids}")
        available_exits = get_room_from_number(available_exits_ids, labyrinth)

        for next_room in available_exits:
            if next_room.get("room_number") not in visited:
                visited.append(next_room.get("room_number"))
                new_path = list(path)
                new_path.append(next_room)
                queue.append(new_path)


def get_room_from_number(rom_numbers, labyrinth):
    rooms = []
    for room in labyrinth:
        if room.get("room_number") in rom_numbers:
            rooms.append(room)
    return rooms