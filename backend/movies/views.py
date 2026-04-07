from .models import Movie, Genre
from rest_framework import permissions, viewsets

from .serializers import MovieSerializer

class MovieViewSet(viewsets.ModelViewSet):
    # Se ordenan las películas por título en orden alfabético
    queryset = Movie.objects.all().order_by("title")
    serializer_class = MovieSerializer
    # Solo los usuarios autenticados pueden acceder a esta vista
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminOrReadOnly] 
