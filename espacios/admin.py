from django.contrib import admin
from .models import Espacio


@admin.register(Espacio)
class EspacioAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
        'tipo',
        'capacidad',
        'precio_por_hora',
        'disponible',
    )
    list_filter = ('tipo', 'disponible')
    search_fields = ('nombre',)