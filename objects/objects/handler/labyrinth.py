from objects.models import *

def load_labyrinth(size):
    labyrinth = Labyrinth.objects.filter(size=size).first()
    if labyrinth == None:
        return

    lab_rooms = Room.objects.filter(labyrinth=labyrinth)
    return lab_rooms
