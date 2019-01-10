from rest_framework import viewsets
from visitante.serializers import VisitanteSerializer
from visitante.models import Visitante

class VisitanteViewSet(viewsets.ModelViewSet):
    """
    API visitante
    """
    queryset = Visitante.objects.all()
    serializer_class = VisitanteSerializer
