from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Labyrinth, Room
from .serializers import LabyrinthSerializer, RoomSerializer


@api_view(['GET'])
def index(request):
    return Response({'message': 'Welcome to Simulus API v1'})


@api_view(['GET'])
def find_labyrinths(request):
    labyrinths = Labyrinth.objects.all()
    serializer = LabyrinthSerializer(labyrinths, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def find_labyrinth_rooms(request, labyrinth_id):
    try:
        rooms = Room.objects.filter(labyrinth=labyrinth_id)
        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data)
    except Room.DoesNotExist:
        return Response({'message': 'No content'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
