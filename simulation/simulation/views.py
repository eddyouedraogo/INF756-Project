from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *

class RuleSetView(APIView):
    def get(self, request, format=None):
        objectives = RuleSet.objects.all()
        serializer  = RuleSetSerializer(objectives, many=True)
        return Response(serializer.data)

class RuleItemView(APIView):
    def get(self, request, format=None):
        objectives = RuleItem.objects.all()
        serializer  = RuleItemSerializer(objectives, many=True)
        return Response(serializer.data)
    
class ActionRuleItemtView(APIView):
    def get(self, request, format=None):
        objectives = ActionRuleItem.objects.all()
        serializer  = ActionRuleItemSerializer(objectives, many=True)
        return Response(serializer.data)
    
class ObjectiveRuleItemtView(APIView):
    def get(self, request, format=None):
        objectives = ObjectiveRuleItem.objects.all()
        serializer  = ObjectiveRuleItemSerializer(objectives, many=True)
        return Response(serializer.data)