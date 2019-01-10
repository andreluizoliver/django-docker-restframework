from rest_framework import serializers
from visitante.models import Visitante

        
class VisitanteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Visitante
        fields = ('url', 'pessoa')
