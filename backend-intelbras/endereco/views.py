from rest_framework import viewsets
from endereco.models import Endereco
from endereco.serializers import EnderecoSerializer


class EnderecoViewSet(viewsets.ModelViewSet):
    """
    API endereco
    """
    queryset = Endereco.objects.all().order_by('tipo_endereco')
    serializer_class = EnderecoSerializer
