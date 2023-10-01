from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from .handler.labyrinth import load_labyrinth
from rest_framework.exceptions import NotFound

class ObjectiveView(APIView):
    def get(self, request, format=None):
        objectives = Objective.objects.all()
        serializer  = ObjectiveSerializer(objectives, many=True)
        return Response(serializer.data)

class LabyrinthView(APIView):
    def get(self, request, format=None):

        labyrinth_size = request.query_params.get('labyrinth_size')

        if labyrinth_size == None: 
            objectives = Labyrinth.objects.all()
            serializer  = LabyrinthSerializer(objectives, many=True)
            return Response(serializer.data)
        else:
            rooms=load_labyrinth(labyrinth_size)
            if rooms == None: 
                raise NotFound(detail=f"{labyrinth_size} Labyrinth not found", code=404)
            
            serializer = RoomSerializer(rooms, many=True)
            return Response(serializer.data)