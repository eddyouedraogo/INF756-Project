from django.db import models


class Objective(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField()


class Room(models.Model):
    room_number = models.IntegerField()
    is_lab_entrance = models.BooleanField()
    is_lab_exit = models.BooleanField()
    available_exits = models.ManyToManyField('self')
    labyrinth = models.ForeignKey('Labyrinth', on_delete=models.CASCADE)

    class Meta:
        db_table = 'objects_room'


class RoomObjective(models.Model):
    objective_id = models.IntegerField()
    room_id = models.IntegerField()


class Labyrinth(models.Model):
    name = models.CharField(max_length=50)
    size = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'objects_labyrinth'


class Mouse(models.Model):
    name = models.CharField(max_length=50)
    intelligence = models.IntegerField()
    health = models.IntegerField()
    mental = models.IntegerField()
    current_room = models.OneToOneField(Room, on_delete=models.SET_NULL, null=True)


class Action(models.Model):
    name = models.CharField(max_length=50)
    intelligence_needed_to_perform = models.IntegerField()
