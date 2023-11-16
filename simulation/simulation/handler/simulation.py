from .api_requests import *
import sys

def create_simulation(payload):
    print("******** Creating Simulation ******")
    labyrinth_info = payload.get("labyrinth")
    rule_set_id = payload.get("ruleSet")

    labyrinth = get_labyrinth(labyrinth_info.get("name"))
    intelligences = get_intelligences()
    action_rules = get_action_rule_for_rule_set(rule_set_id.get("id"))
    objective_rules = get_objective_rule_for_rule_set(rule_set_id.get("id"))

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