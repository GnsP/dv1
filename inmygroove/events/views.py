from django.shortcuts import render
from rest_framework import viewsets
from .serializers import EventSerializers
from .models import Event

# Create your views here.
class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializers
    queryset = Event.objects.all()
    
