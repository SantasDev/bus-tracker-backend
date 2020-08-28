from django.db import models

# Create your models here.

class Station (models.Model):
    name = models.CharField(max_length=100)
    longitude = models.FloatField()
    latitude = models.FloatField()
    direction = models.CharField(max_length=100)

    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Route (models.Model):
    reference = models.CharField(max_length=10)
    spend_time = models.DecimalField(max_digits=120, decimal_places=1)
    stations = models.ManyToManyField(Station)

    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} ({})'.format(self.reference, self.spend_time)

class Traject (models.Model):
    driver = models.CharField(max_length=100)
    bus = models.CharField(max_length=100)
    route = models.ForeignKey(Route, on_delete=models.SET_NULL, null=True)

    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)