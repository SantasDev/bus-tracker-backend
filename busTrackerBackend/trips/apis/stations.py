from trips.models import Station
from rest_framework import serializers, viewsets

class StationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Station
        fields = ['id','name', 'longitude', 'latitude', 'direction']

# ViewSets define the view behavior.
class StationViewSet(viewsets.ModelViewSet):
    queryset = Station.objects.all()
    serializer_class = StationSerializer
