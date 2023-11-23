from rest_framework import serializers
from .models import *

class ObjectiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Objective
        fields = '__all__'

class LabyrinthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Labyrinth
        fields = '__all__'

class RoomSerializer(serializers.Serializer):
    room_number = serializers.IntegerField()
    is_lab_entrance = serializers.BooleanField()
    is_lab_exit = serializers.BooleanField()
    available_exits = serializers.JSONField(default=[])
    labyrinth = serializers.IntegerField()
    objective_id = serializers.IntegerField(allow_null=True)
    
class RoomObjectiveSerializer(serializers.Serializer):
    room_id = serializers.IntegerField()
    objective_id = serializers.IntegerField()
    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     representation['labyrinth'] = LabyrinthSerializer(instance.labyrinth).data
    #     return representation
