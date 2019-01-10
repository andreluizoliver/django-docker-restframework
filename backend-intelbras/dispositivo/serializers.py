from rest_framework import serializers

from dispositivo.models import Dispositivo


class DispositivoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dispositivo
        fields = ('url', 'nome', 'possui_senha', 'senha', 'tipo_controle', 'troca_bidirecional', 'sincronismo_hora', 'area', 'excluir_dados', 'modo_comunicacao', 'ip', 'porta', 'endereco', 'baud_rate')