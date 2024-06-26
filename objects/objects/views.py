from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from .models import *
from .serializers import *
from objects.handler.labyrinth import *
from drf_yasg.utils import swagger_auto_schema


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
    @swagger_auto_schema(responses={200: ObjectiveSerializer(many=True)})
    def get(self, request, format=None):
        """
        Retourne la liste des objectifs disponibles.
        """
        objectives = Objective.objects.all()
        serializer  = ObjectiveSerializer(objectives, many=True)
        return Response(serializer.data)

class LabyrinthView(APIView):
    # @swagger_auto_schema(manual_parameters=[
    #     {
    #         "name" : "labyrinth_size",
    #         "in_": "query",
    #         "description" : "Taille du labyrinthe désirée",
    #         "required" : False,
    #         "type" : "string"
    #     },
    #     {
    #         "name" : "labyrinth_id",
    #         "in_": "query",
    #         "description" : "identifiant du labyrinthe désirée",
    #         "required" : False,
    #         "type" : "string"
    #     }
    # ])
    def get(self, request, format=None):

        """
        Retourne la liste des labyrinthes disponibles.
        Si un paramètre est envoyé, seulement le labyrinthe spécifié en paramètre sera retourné.
        """

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

class RoomObjectiveView(APIView):
    def get(self, request):
        """
        Retourne la liste des pièces avec des objectifs et les objectifs qui y sont.
        Si l'id du labyrinthe est mentionné, seulement les pièces de ce labyrinthe seront retournées.
        ---
        serializer: RoomObjectiveSerializer
        omit_serializer: false
        many: true
        parameters:
        - name: labyrinth_id
          description: identifiant du labyrinthe désirée
          required: false
          type: string
          paramType: query
        """
        labyrinth_id = request.query_params.get('labyrinth_id')
        if labyrinth_id:
            rooms = load_labyrinth_for_id(labyrinth_id)
            room_ids = [room.get("id") for room in rooms]
            rooms_objectives = RoomObjective.objects.filter(room_id__in=room_ids)
        else:
            rooms_objectives = RoomObjective.objects.all().values()

        serializer = RoomObjectiveSerializer(rooms_objectives, many=True)
        return Response(list(serializer.data))