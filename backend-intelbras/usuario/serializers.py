from rest_framework import serializers
from usuario.models import Usuario

        
class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = ('url', 'pessoa', 'departamento', 'tipo_usuario', 'data_contratacao')
