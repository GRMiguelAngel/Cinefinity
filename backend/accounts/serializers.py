from django.contrib.auth.models import Group, User
from rest_framework import serializers


class GroupSerializer(serializers.HyperlinkedModelSerializer): # Uso de Hyperlinked para una mejor navegación en la API
    # Serialización de los groups
    
    class Meta:
        model = Group
        fields = ["url", "name"]


class UserSerializer(serializers.HyperlinkedModelSerializer): # Uso de Hyperlinked para una mejor navegación en la API
    # Serialización de los users

    groups = GroupSerializer(many=True, read_only=True) # Se muestran todos los parametros de groups
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]