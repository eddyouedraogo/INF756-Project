from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from .models import *
from .serializers import LabyrinthSerializer, RoomSerializer, ObjectiveSerializer
from objects.handler.labyrinth import *



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

class ObjectiveView(APIView):
    def get(self, request, format=None):
        objectives = Objective.objects.all()
        serializer  = ObjectiveSerializer(objectives, many=True)
        return Response(serializer.data)

class LabyrinthView(APIView):
    def get(self, request, format=None):

        labyrinth_size = request.query_params.get('labyrinth_size')
        labyrinth_id = request.query_params.get('labyrinth_id')

        if labyrinth_size == None and labyrinth_id == None: 
            objectives = Labyrinth.objects.all()
            serializer  = LabyrinthSerializer(objectives, many=True)
            return Response(serializer.data)
        elif labyrinth_size:
            rooms=load_labyrinth_for_size(labyrinth_size)
            if rooms == None: 
                raise NotFound(detail=f"{labyrinth_size} Labyrinth not found", code=404)
            
            serializer = RoomSerializer(rooms, many=True)
            return Response(serializer.data)
        elif labyrinth_id:
            rooms=load_labyrinth_for_id(labyrinth_id)
            if rooms == None: 
                raise NotFound(detail=f"{labyrinth_size} Labyrinth not found", code=404)
            
            serializer = RoomSerializer(rooms, many=True)
            return Response(serializer.data)