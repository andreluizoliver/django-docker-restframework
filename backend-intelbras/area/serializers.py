from area.models import Area
from rest_framework import serializers

class AreaSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Area
        fields = ('url', 'nome', 'numero', 'area_principal')