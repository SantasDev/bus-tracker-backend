from rest_framework import serializers, viewsets

from trips.models import Route
from trips.apis.stations import StationSerializer

class RouteSerializer(serializers.HyperlinkedModelSerializer):
    stations =  StationSerializer(many=True, read_only=True)
    class Meta:
        model = Route
        fields = ['id','reference', 'spend_time', 'stations']

# ViewSets define the view behavior.
class RouteViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
