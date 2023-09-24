from django.db import models


class Objective(models.Model): 
    name = models.CharField(max_length=50)
    description = models.CharField()
    effect_on_health = models.IntegerField()
    effect_on_mental = models.IntegerField()
    effect_on_intelligence = models.IntegerField()
    room = models.ForeignKey('Room', on_delete=models.SET_NULL, null=True) # Many to One relationship; an objective has a room and a room has many objective

class Room(models.Model):
    room_number = models.IntegerField()
    is_lab_entrance = models.BooleanField()
    is_lab_exit = models.BooleanField()
    available_exit = models.ForeignKey('self', on_delete=models.CASCADE)
    labyrinth = models.ForeignKey('Labyrinth', on_delete=models.CASCADE)

class Labyrinth(models.Model):
    name = models.CharField(max_length=50)
    size = models.CharField(max_length=20)

class Mouse(models.Model):
    name = models.CharField(max_length=50)
    intelligence = models.IntegerField()
    health = models.IntegerField()
    mental = models.IntegerField()
    current_room = models.OneToOneField(Room, on_delete=models.SET_NULL, null=True)

class Action(models.Model):
    name = models.CharField(max_length=50)
    intelligence_needed_to_perform = models.IntegerField()
    effect_on_health = models.IntegerField()
    effect_on_mental = models.IntegerField()