from django.db import models



# Create your models here.

class BusDriver (models.Model):

    license_id = models.CharField(max_length=100, blank=True)
    rate = models.DecimalField(max_digits=10, decimal_places=1, default=0)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)