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
