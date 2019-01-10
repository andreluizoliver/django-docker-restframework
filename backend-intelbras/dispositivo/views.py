from rest_framework import viewsets

from dispositivo.models import Dispositivo
from dispositivo.serializers import DispositivoSerializer


class DispositivoViewSet(viewsets.ModelViewSet):
    """
    API dispositivo
    """
    queryset = Dispositivo.objects.all().order_by('nome')
    serializer_class = DispositivoSerializer