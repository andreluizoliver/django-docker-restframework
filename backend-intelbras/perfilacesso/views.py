from rest_framework import viewsets

from perfilacesso.models import PerfilAcesso
from perfilacesso.serializers import PerfilAcessoSerializer


class PerfilAcessoViewSet(viewsets.ModelViewSet):
    """
    API perfil acesso
    """
    queryset = PerfilAcesso.objects.all().order_by('nome')
    serializer_class = PerfilAcessoSerializer
