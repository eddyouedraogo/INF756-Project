from .api_requests import *


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
    parents = [labyrinth[0]]
    dfs_intelligence(visited_dfs, labyrinth, labyrinth[0], labyrinth[0], parents, False)
    print(f"dfs visited {len(visited_dfs)} nodes")
    path = bfs_intelligence(visited_bfs, labyrinth, labyrinth[0], queue_bfs)
    print(f"bfs visited {len(visited_bfs)} nodes")
    route = [room.get("room_number") for room in path]
    # bfs_stupid_mouse(visited_bfs_stupid, labyrinth, labyrinth[0], queue_bfs_stupid)

    return {
        "visited_dfs": visited_dfs,
        "visited_bfs": route,
        "bfs_stupid_mouse": visited_bfs_stupid,
        }

def dfs_intelligence(visited, labyrinth, room, parent, parents, exit_found):
    if parents and parent:
        last_parent = parents[-1]
        last_parent_id = last_parent.get("room_number")
        current_room_id = room.get("room_number")
        if last_parent_id != current_room_id:
            print(f"adding parent {last_parent_id} to room {current_room_id}")
            parents.append(parent)
    elif parent and not parents: 
        parents.append(parent)


    if (room.get("room_number") not in visited):
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

            # for next_room in available_exits:
            #     if not exit_found:
            #         node = next_room.get("room_number")
            #         print("Mouse is visiting next node", node)
            #         exit_found = dfs_intelligence(visited, labyrinth, next_room, room, parents, exit_found)
            # return exit_found
        
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
    print("parents are ", [p.get("room_number") for p in parents] )

    current_parent = parents.pop()

    visited.append(current_parent.get("room_number"))
    parent_room_number = current_parent.get("room_number")
    print (f"Mouse backtracked to {parent_room_number}")
    
    available_exits_ids = current_parent.get("available_exits")
    print (f"Parents Available Exists are {available_exits_ids}")

    last_n_rooms = visited[-30:]
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


def bfs_intelligence(visited, labyrinth, room, queue): 
    visited.append(room.get("room_number"))
    queue.append([room])
    exit_found = False
    
    while (queue and not exit_found):     
        path = queue.pop(0) 
        # print (current_room, end = " ") 
        current_room = path[-1]
        if current_room.get("is_lab_exit"):
            exit_found = True
            return path
        
        available_exits_ids = current_room.get("available_exits")
        # print (f"Available Exists are {available_exits_ids}")
        available_exits = get_room_from_number(available_exits_ids, labyrinth)

        for next_room in available_exits:
            new_path = list(path)
            new_path.append(next_room)
            queue.append(new_path)

            # if next_room.get("room_number") not in visited:
            #     visited.append(next_room.get("room_number"))
            #     queue.append(next_room)
                
            #     if next_room.get("is_lab_exit"):
            #         exit_found = True
            #         print("Mouse has reached the exit")
            #         # break

def random_search(visited, labyrinth, room, queue, previous_room, exit_found):
    if room.get("id") not in visited:
        visited.append(room.get("room_number"))
        queue.append(room)
    
        print (f"Visited {visited}")
        print (f"Queued {queue}")
        print (f"Previous Room {previous_room}")
        while(not exit_found):
            
            print (f"Currently visiting {room}")

            available_exits_ids = room.get("available_exits")
            print (f"Available Exists are {available_exits_ids}")
            available_exits = get_room_from_number(available_exits_ids, labyrinth)

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
                available_exits = get_room_from_number(available_exits_to_be_visited, labyrinth)
                next_room = available_exits.pop(0)
                random_search(visited, labyrinth, next_room, queue, previous_room, next_room.get("is_lab_exit"))


def bfs_stupid_mouse(visited, labyrinth, room, queue): 
    visited.append(room.get("room_number"))
    queue.append(room)
    exit_found = False
    
    while (queue and not exit_found):     
        current_room = queue.pop(0) 
        # print (current_room, end = " ") 
        
        available_exits_ids = current_room.get("available_exits")
        # print (f"Available Exists are {available_exits_ids}")
        available_exits = get_room_from_number(available_exits_ids, labyrinth)

        for next_room in available_exits:
            visited.append(next_room.get("room_number"))
            queue.append(next_room)
                
            if next_room.get("is_lab_exit"):
                exit_found = True
                # print("Mouse has reached the exit")
                break

def get_room_from_number(rom_numbers, labyrinth):
    rooms = []
    for room in labyrinth:
        if room.get("room_number") in rom_numbers:
            rooms.append(room)
    return rooms