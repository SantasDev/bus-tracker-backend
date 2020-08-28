from django.contrib import admin
from trips.models import Station,Route,Traject

# Register your models here.

admin.site.register(Station)
admin.site.register(Route)
admin.site.register(Traject)