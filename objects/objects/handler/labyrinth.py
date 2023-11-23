from objects.models import *

def load_labyrinth_for_size(size):
    labyrinth = Labyrinth.objects.filter(size=size).first()
    if labyrinth == None:
        return

    lab_rooms = Room.objects.filter(labyrinth=labyrinth).order_by('-is_lab_entrance')
    room_ids = [room.id for room in lab_rooms]
    rooms_objectives = load_room_objectives(room_ids)
    
    return join_objectives_to_rooms(lab_rooms, rooms_objectives)

def load_labyrinth_for_id(id):
    labyrinth = Labyrinth.objects.filter(id=id).first()
    if labyrinth == None:
        return

    lab_rooms = Room.objects.filter(labyrinth=labyrinth).order_by('-is_lab_entrance')
    room_ids = [room.id for room in lab_rooms]
    rooms_objectives = load_room_objectives(room_ids)
    
    return join_objectives_to_rooms(lab_rooms, rooms_objectives)

def load_room_objectives(room_ids):
    rooms_objectives = RoomObjective.objects.filter(room_id__in=room_ids)
    return rooms_objectives

def join_objectives_to_rooms(lab_rooms, rooms_objectives):
    ret = []
    for lab_room in lab_rooms:
        current_room = {
            "id": lab_room.id,
            "room_number": lab_room.room_number,
            "is_lab_entrance": lab_room.is_lab_entrance,
            "is_lab_exit": lab_room.is_lab_exit,
            "available_exits": lab_room.available_exits,
            "labyrinth": lab_room.labyrinth.id
        }
        
        for room in rooms_objectives : 
            if lab_room.id == room.room_id:
                current_room["objective_id"] = room.objective_id
        
        ret.append(current_room)

    return ret