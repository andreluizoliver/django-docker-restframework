from django.contrib.auth.models import User, Group, Permission
from rest_framework import serializers

class OperadorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'password', 'email', 'groups', 'is_staff', 'is_active', 'is_superuser')
        
    def create(self, validated_data):
        user = super(OperadorSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
        
class PerfilSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name', 'permissions')
        
class PermissaoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Permission
        fields = ('url', 'name')