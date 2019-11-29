from rest_framework import serializers
from .models import Event
class EventSerializers(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ("id","title", "id_num", "organiser", "location", "date", "time", "event_about", "event_image")