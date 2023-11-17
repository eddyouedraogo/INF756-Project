from .api_requests import *
import sys

def create_simulation(payload):
    print("******** Creating Simulation ******")
    labyrinth_id = payload.get("labyrinth_id")
    rule_set_id = payload.get("ruleSet_id")

    labyrinth = get_labyrinth(labyrinth_id)
    intelligences = get_intelligences()
    action_rules = get_action_rule_for_rule_set(rule_set_id)
    objective_rules = get_objective_rule_for_rule_set(rule_set_id)

    ret = {
        "labyrinth": labyrinth,
        "intelligences": intelligences,
        "action_rules": action_rules,
        "objective_rules": objective_rules
    }

    
    visited_dfs = []
    queue_bfs = []
    queue_bfs_stupid = []
    visited_bfs = []
    visited_bfs_stupid = []
    dfs_intelligence(visited_dfs, labyrinth, labyrinth[0])
    bfs_intelligence(visited_bfs, labyrinth, labyrinth[0], queue_bfs)
    bfs_stupid_mouse(visited_bfs_stupid, labyrinth, labyrinth[0], queue_bfs_stupid)

    return {
        "visited_dfs": visited_dfs,
        "visited_bfs": visited_bfs,
        "bfs_stupid_mouse": visited_bfs_stupid,
        }

def dfs_intelligence(visited, labyrinth, room):
    if room.get("id") not in visited:
        print ("The mouse is currently in room ", room.get("id"))
        visited.append(room.get("id"))

        if room.get("is_lab_exit"):
            print("Mouse has reached the exit")
            return True
        
        available_exits_ids = room.get("available_exits")
        print (f"Available Exists are {available_exits_ids}")
        available_exits = get_room_from_ids(available_exits_ids, labyrinth)
        
        #Si la souris est dans une impasse il faut noter qu'elle est revenue en arriere
        if len(available_exits_ids) == 1 and available_exits_ids[0] in visited:
            visited.append(available_exits_ids[0])

        for next_room in available_exits:
            exit_found = dfs_intelligence(visited, labyrinth, next_room)
            if exit_found:
                return exit_found

def bfs_intelligence(visited, labyrinth, room, queue): 
    visited.append(room.get("id"))
    queue.append(room)
    exit_found = False
    
    while (queue and not exit_found):     
        current_room = queue.pop(0) 
        # print (current_room, end = " ") 
        
        available_exits_ids = current_room.get("available_exits")
        # print (f"Available Exists are {available_exits_ids}")
        available_exits = get_room_from_ids(available_exits_ids, labyrinth)

        for next_room in available_exits:
            
            if next_room.get("id") not in visited:
                visited.append(next_room.get("id"))
                queue.append(next_room)
                
                if next_room.get("is_lab_exit"):
                    exit_found = True
                    # print("Mouse has reached the exit")
                    # break

def random_search(visited, labyrinth, room, queue, previous_room, exit_found):
    if room.get("id") not in visited:
        visited.append(room.get("id"))
        queue.append(room)
    
        print (f"Visited {visited}")
        print (f"Queued {queue}")
        print (f"Previous Room {previous_room}")
        while(not exit_found):
            
            print (f"Currently visiting {room}")

            available_exits_ids = room.get("available_exits")
            print (f"Available Exists are {available_exits_ids}")
            available_exits = get_room_from_ids(available_exits_ids, labyrinth)

            if(len(available_exits) > 1):
                for next_room in available_exits: 
                    print (f"Visiting next {next_room}")
                    random_search(visited, labyrinth, next_room, queue, room, next_room.get("is_lab_exit"))
            elif previous_room:
                print (f"No exit ! Going back to previous room next {previous_room}")
                available_exits_ids = previous_room.get("available_exits")

                #Get available exits except the ones we already visited 
                available_exits_to_be_visited = list(set(visited) - list(available_exits_ids))
            
                # print (f"Available Exists are {available_exits_ids}")
                available_exits = get_room_from_ids(available_exits_to_be_visited, labyrinth)
                next_room = available_exits.pop(0)
                random_search(visited, labyrinth, next_room, queue, previous_room, next_room.get("is_lab_exit"))


def bfs_stupid_mouse(visited, labyrinth, room, queue): 
    visited.append(room.get("id"))
    queue.append(room)
    exit_found = False
    
    while (queue and not exit_found):     
        current_room = queue.pop(0) 
        # print (current_room, end = " ") 
        
        available_exits_ids = current_room.get("available_exits")
        # print (f"Available Exists are {available_exits_ids}")
        available_exits = get_room_from_ids(available_exits_ids, labyrinth)

        for next_room in available_exits:
            visited.append(next_room.get("id"))
            queue.append(next_room)
                
            if next_room.get("is_lab_exit"):
                exit_found = True
                # print("Mouse has reached the exit")
                break

def get_room_from_ids(ids, labyrinth):
    rooms = []
    for room in labyrinth:
        if room.get("id") in ids:
            rooms.append(room)
    return rooms