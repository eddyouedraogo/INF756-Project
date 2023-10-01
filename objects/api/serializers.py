from rest_framework.serializers import ModelSerializer
from .models import Labyrinth, Room


class LabyrinthSerializer(ModelSerializer):
    class Meta:
        model = Labyrinth
        fields = '__all__'


class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['labyrinth'] = LabyrinthSerializer(instance.labyrinth).data
        return representation
