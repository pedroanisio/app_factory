from rest_framework import viewsets
from .models import AppDefinition
from .serializers import AppDefinitionSerializer

class AppDefinitionViewSet(viewsets.ModelViewSet):
    queryset = AppDefinition.objects.all()
    serializer_class = AppDefinitionSerializer
