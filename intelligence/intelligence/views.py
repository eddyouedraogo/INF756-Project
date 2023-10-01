from intelligence.models import Intelligence
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import IntelligenceSerializer

class IntelligenceView(APIView):
    def get(self, request, format=None):
        intelligences= Intelligence.objects.all()
        serializer = IntelligenceSerializer(intelligences, many=True)
        return Response(serializer.data)