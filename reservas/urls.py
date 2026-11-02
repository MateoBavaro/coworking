from django.urls import path
from .views import cancelar_reserva, crear_reserva, lista_reservas

urlpatterns = [
    path('', lista_reservas, name='lista_reservas'),
    path('nueva/', crear_reserva, name='crear_reserva'),
    path('cancelar/<int:reserva_id>/', cancelar_reserva, name='cancelar_reserva'),
]