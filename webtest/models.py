from django.db import models


class TrafficLight(models.Model):
    text = models.CharField(max_length=100)
    duration = models.TimeField(null=True, blank=True)
