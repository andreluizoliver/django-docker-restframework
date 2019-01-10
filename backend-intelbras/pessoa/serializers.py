from pessoa.models import Pessoa
from rest_framework import serializers

class PessoaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pessoa
        fields = ('url', 'nome', 'sobrenome', 'sexo', 'email', 'telefone_celular', 'telefone_residencial', 'telefone_comercial', 'data_nascimento', 'cpf', 'estado_civil', 'rg', 'nacionalidade', 'foto')