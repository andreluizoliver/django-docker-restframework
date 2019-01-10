from zonatempo.models import ZonaTempo, Tempo
from rest_framework import serializers

class ZonaTempoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ZonaTempo
        fields = ('url', 'nome', 'descricao')
        
class TempoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tempo
        fields = ('url', 'zona_tempo', 'dia_semana', 'inicio', 'fim')