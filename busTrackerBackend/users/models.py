from django.contrib.auth.models import User

from django.db import models

# Create your models here.

class BtUser(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    contract = models.CharField(max_length=100, blank=True)
    enterprise = models.CharField(max_length=100, blank=True)
    role = models.CharField(max_length=100, blank=True)

    Created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)