from rest_framework import serializers
from .models import *

class RuleSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = RuleSet
        fields = '__all__'

class RuleItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = RuleItem
        fields = '__all__'

class ActionRuleItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActionRuleItem
        fields = '__all__'

class ObjectiveRuleItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObjectiveRuleItem
        fields = '__all__'

class MousesIntelligenceSerializer(serializers.Serializer):
    intelligence_id = serializers.IntegerField(required=True)
    number_of_mouses = serializers.IntegerField(required=True)


class CreateSimulationSerializer(serializers.Serializer):
    mouses_intelligence = serializers.ListField(child=MousesIntelligenceSerializer())
    labyrinth_id = serializers.IntegerField(required=True)
    ruleSet_id = serializers.IntegerField(required=True)

