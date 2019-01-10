from rest_framework import viewsets
from usuario.serializers import UsuarioSerializer
from usuario.models import Usuario

class UsuarioViewSet(viewsets.ModelViewSet):
    """
    API usuario
    """
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
