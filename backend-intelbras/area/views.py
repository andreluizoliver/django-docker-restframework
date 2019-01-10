from rest_framework import viewsets

from area.models import Area
from area.serializers import AreaSerializer


class AreaViewSet(viewsets.ModelViewSet):
    """
    API area
    """
    queryset = Area.objects.all().order_by('nome')
    serializer_class = AreaSerializer