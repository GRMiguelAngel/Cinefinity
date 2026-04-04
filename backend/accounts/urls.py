from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
'''
    Se crea un router para manejar las rutas de la API de manera automática.
    Para que funcione tiene que estar definido el viewset correspondiente en views.py y registrado en el router.
'''
router.register(r"users", views.UserViewSet) # Se registra el viewset de users en el router
router.register(r"groups", views.GroupViewSet) # Se registra el viewset de groups en el router

urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")), # Se incluye la ruta para la autenticación de la API
]