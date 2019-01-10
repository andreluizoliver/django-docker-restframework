from rest_framework import viewsets
from departamento.models import Departamento
from departamento.serializers import DepartamentoSerializer


class DepartamentoViewSet(viewsets.ModelViewSet):
    """
    API departamento
    """
    queryset = Departamento.objects.all().order_by('nome')
    serializer_class = DepartamentoSerializer
