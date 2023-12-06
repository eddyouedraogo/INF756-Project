from intelligence.models import Intelligence
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import IntelligenceSerializer

class IntelligenceView(APIView):
    """
    Intelligence API.
    Gère les informations reliées à l'intelligence
    """
    def get(self, request, format=None):
        """
        Retourne la liste des intelligences disponibles.
        """
        intelligences= Intelligence.objects.all()
        serializer = IntelligenceSerializer(intelligences, many=True)
        return Response(serializer.data)