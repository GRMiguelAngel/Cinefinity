from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
'''
    Se crea un router para manejar las rutas de la API de manera automática.
    Para que funcione tiene que estar definido el viewset correspondiente en views.py y registrado en el router.
'''
router.register(r"", views.MovieViewSet) # Se registra el viewset de users en el router

urlpatterns = [
    path("", include(router.urls)),
]