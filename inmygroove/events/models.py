from django.db import models

# Create your models here.

class Event(models.Model):



    title = models.CharField(max_length=120)
    id_num = models.PositiveIntegerField()
    organiser = models.CharField(max_length=120)
    location = models.CharField(max_length=120)
    date = models.DateField()
    time = models.DateTimeField()
    event_about = models.TextField()
    event_image = models.FileField()

    def __str__(self):      #i think __ double instead of _
        return "Event for {}".format(self.name)

