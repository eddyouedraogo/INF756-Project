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

class MouseSerializer(serializers.Serializer):
    intelligence = serializers.CharField(required=True)

class LabyrinthSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)

class RuleSetSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)

class CreateSimulationSerializer(serializers.Serializer):
    mouses = serializers.ListField(child=MouseSerializer())
    labyrinth = LabyrinthSerializer(required=True)
    ruleSet = RuleSetSerializer(required=True)

