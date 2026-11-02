from django.urls import path
from .views import crear_cliente, lista_clientes

urlpatterns = [
    path('', lista_clientes, name='lista_clientes'),
    path('nuevo/', crear_cliente, name='crear_cliente'),
]