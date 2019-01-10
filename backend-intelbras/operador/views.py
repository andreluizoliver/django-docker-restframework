from django.contrib.auth.models import User, Group, Permission
from rest_framework import viewsets
from operador.serializers import OperadorSerializer, PerfilSerializer, \
    PermissaoSerializer


class OperadorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = OperadorSerializer

class PerfilViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = PerfilSerializer
    
class PermissaoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows permissions to be viewed or edited.
    """
    queryset = Permission.objects.all()
    serializer_class = PermissaoSerializer
