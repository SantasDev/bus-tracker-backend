from users.models import BtUser

from django.db import models

# Create your models here.

class BtAdmin (models.Model):

    user = models.OneToOneField(BtUser, on_delete=models.CASCADE)
    terminal_id = models.CharField(max_length=100, blank=True)

