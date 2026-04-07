from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets

from accounts.serializers import GroupSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    # Se ordenan los usuarios por fecha de creación, mostrando primero los más recientes
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    # Solo los usuarios autenticados pueden acceder a esta vista
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminOrReadOnly] 
class GroupViewSet(viewsets.ModelViewSet):
    # Se ordenan los grupos por nombre en orden alfabético
    queryset = Group.objects.all().order_by("name")
    serializer_class = GroupSerializer
    # Solo los usuarios autenticados pueden acceder a esta vista
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminOrReadOnly]