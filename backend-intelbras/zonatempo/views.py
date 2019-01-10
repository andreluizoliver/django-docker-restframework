from rest_framework import viewsets
from zonatempo.serializers import ZonaTempoSerializer, TempoSerializer
from zonatempo.models import ZonaTempo, Tempo

class ZonaTempoViewSet(viewsets.ModelViewSet):
    """
    API zona tempo
    """
    queryset = ZonaTempo.objects.all().order_by('nome')
    serializer_class = ZonaTempoSerializer
    
class TempoViewSet(viewsets.ModelViewSet):
    """
    API tempo
    """
    queryset = Tempo.objects.all().order_by('zona_tempo')
    serializer_class = TempoSerializer
