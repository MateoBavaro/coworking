from django.urls import path
from .views import lista_espacios

urlpatterns = [
    path('', lista_espacios, name='lista_espacios'),
]