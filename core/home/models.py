from django.db import models
from datetime import datetime

class Event(models.Model):
    name = models.CharField(max_length=100)
    event_date = models.DateTimeField(default= datetime.now)  # Add event_date field


    def __str__(self):
        return self.name