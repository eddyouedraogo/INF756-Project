from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from .handler.simulation import *

class RuleSetView(APIView):
    def get(self, request, format=None):
        ruleSets = RuleSet.objects.all()
        serializer  = RuleSetSerializer(ruleSets, many=True)
        return Response(serializer.data)

class RuleItemView(APIView):
    def get(self, request, format=None):
        ruleItems = RuleItem.objects.all()
        serializer  = RuleItemSerializer(ruleItems, many=True)
        return Response(serializer.data)
    
class ActionRuleItemtView(APIView):
    def get(self, request, format=None):
        actionRuleItems = ActionRuleItem.objects.all()
        serializer  = ActionRuleItemSerializer(actionRuleItems, many=True)
        return Response(serializer.data)
    
class ObjectiveRuleItemtView(APIView):
    def get(self, request, format=None):
        objectiveRulesItems = ObjectiveRuleItem.objects.all()
        serializer  = ObjectiveRuleItemSerializer(objectiveRulesItems, many=True)
        return Response(serializer.data)
    

class SimulationView(APIView):
    def post(self, request):
        payload = request.data
        serializer = CreateSimulationSerializer(data=payload)
        if serializer.is_valid():
            data = create_simulation(payload)
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Payload is wrong'}, status=status.HTTP_400_BAD_REQUEST)
        

class RuleSetAndItemView(APIView):
    def get(self, request):
        data = []

        objectiveRulesItems = ObjectiveRuleItem.objects.all()
        filteredByRuleSet = ObjectiveRuleItem.objects.distinct("ruleSet")
        actionRuleItems = ActionRuleItem.objects.all()

        for ori in filteredByRuleSet:
            print("ori.ruleSet", ori.ruleSet)
            ruleSet = {
                "id": ori.ruleSet.id,
                "name": ori.ruleSet.name,
                "items": get_items(objectiveRulesItems, actionRuleItems, ori.ruleSet.id)
            }
            data.append(ruleSet)

        return Response(data)


def get_items(objectiveRulesItems, actionRuleItems, ruleSetId):
    actionRules = get_rule_setItems(actionRuleItems, ruleSetId)
    objectiveRules = get_rule_setItems(objectiveRulesItems, ruleSetId)
    return actionRules + objectiveRules

def get_rule_setItems(ruleItems, ruleSetId):
    ret = []
    for rule in ruleItems:
        if rule.ruleSet.id == ruleSetId:
            data = {
                "id": rule.ruleItem.id,
                "description": rule.ruleItem.description,
                "effect_on_health": rule.effect_on_health,
                "effect_on_mental": rule.effect_on_mental,
                "effect_on_intelligence": rule.effect_on_intelligence,
            }
            ret.append(data)
    return ret
