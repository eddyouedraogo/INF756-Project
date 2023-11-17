from objects.models import *

def load_labyrinth_for_size(size):
    labyrinth = Labyrinth.objects.filter(size=size).first()
    if labyrinth == None:
        return

    lab_rooms = Room.objects.filter(labyrinth=labyrinth).order_by('-is_lab_entrance')
    return lab_rooms

def load_labyrinth_for_id(id):
    labyrinth = Labyrinth.objects.filter(id=id).first()
    if labyrinth == None:
        return

    lab_rooms = Room.objects.filter(labyrinth=labyrinth).order_by('-is_lab_entrance')
    return lab_rooms