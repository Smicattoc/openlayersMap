from django.db import models

class PointFeature(models.Model):
    longitude = models.FloatField()
    latitude = models.FloatField()
