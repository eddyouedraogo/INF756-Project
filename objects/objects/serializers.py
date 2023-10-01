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

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'