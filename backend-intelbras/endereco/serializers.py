from rest_framework import serializers
from endereco.models import Endereco

class EnderecoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Endereco
        fields = ('url', 'pessoa', 'tipo_endereco', 'uf', 'cidade', 'cep', 'rua', 'numero', 'bairro', 'complemento')
