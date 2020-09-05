from django.urls import path
from .apis import trips

urlpatterns = [
    path('list/', trips.get_trips),
    path('create/', trips.create_trip),
    path('edit/<int:id>', trips.edit_trip)
]