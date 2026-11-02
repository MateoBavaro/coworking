from django.contrib import admin
from .models import Reserva


@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'espacio', 'fecha_inicio', 'fecha_fin', 'estado')
    list_filter = ('estado', 'fecha_inicio')
    search_fields = ('cliente__nombre', 'cliente__dni', 'espacio__nombre')
    date_hierarchy = 'fecha_inicio'