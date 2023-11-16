from objects.models import *

def load_labyrinth(size):
    labyrinth = Labyrinth.objects.filter(size=size).first()
    if labyrinth == None:
        return

    lab_rooms = Room.objects.filter(labyrinth=labyrinth).order_by('-is_lab_entrance')
    return lab_rooms
