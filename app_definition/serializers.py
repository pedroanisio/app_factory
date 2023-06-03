from rest_framework import serializers
from .models import AppDefinition

class AppDefinitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppDefinition
        fields = '__all__'
