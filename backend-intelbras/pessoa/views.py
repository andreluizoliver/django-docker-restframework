from rest_framework import viewsets

from pessoa.models import Pessoa
from pessoa.serializers import PessoaSerializer


class PessoaViewSet(viewsets.ModelViewSet):
    """
    API pessoa
    """
    queryset = Pessoa.objects.all().order_by('nome')
    serializer_class = PessoaSerializer
