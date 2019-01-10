from rest_framework import serializers

from perfilacesso.models import PerfilAcesso


class PerfilAcessoSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = PerfilAcesso
        fields = ('url', 'nome', 'zona_tempo', 'usar_visitas', 'dispositivos', 'usuarios', 'visitantes')
