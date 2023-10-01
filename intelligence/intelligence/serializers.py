from rest_framework import serializers
from .models import Intelligence

class IntelligenceSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Intelligence
        fields = '__all__'
