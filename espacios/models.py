from django.core.exceptions import ValidationError
from django.db import models


class Espacio(models.Model):
    TIPO_CHOICES = [
        ('escritorio', 'Escritorio Individual'),
        ('sala', 'Sala de Reuniones'),
        ('oficina', 'Oficina Privada'),
    ]

    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    capacidad = models.PositiveIntegerField()
    precio_por_hora = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)

    def clean(self):
        super().clean()
        if self.precio_por_hora is not None and self.precio_por_hora <= 0:
            raise ValidationError(
                {'precio_por_hora': 'El precio por hora debe ser mayor a 0.'}
            )

    def __str__(self):
        return f'{self.nombre} - {self.get_tipo_display()} (${self.precio_por_hora}/h)'
