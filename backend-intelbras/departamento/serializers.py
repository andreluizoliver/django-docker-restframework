from departamento.models import Departamento
from rest_framework import serializers

class DepartamentoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Departamento
        fields = ('url', 'nome', 'numero', 'departamento_principal')