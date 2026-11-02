from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from clientes.models import Cliente
from espacios.models import Espacio


class Reserva(models.Model):
    ESTADO_CHOICES = [
        ('confirmada', 'Confirmada'),
        ('cancelada', 'Cancelada'),
        ('completada', 'Completada'),
    ]

    cliente = models.ForeignKey(
        Cliente, on_delete=models.CASCADE, related_name='reservas'
    )
    espacio = models.ForeignKey(
        Espacio, on_delete=models.CASCADE, related_name='reservas'
    )
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    estado = models.CharField(
        max_length=20, choices=ESTADO_CHOICES, default='confirmada'
    )
    creado_el = models.DateTimeField(auto_now_add=True)

    def clean(self):
        super().clean()

        # 1. Validar fechas lógicas
        if (
            self.fecha_inicio
            and self.fecha_fin
            and self.fecha_fin <= self.fecha_inicio
        ):
            raise ValidationError({
                'fecha_fin': (
                    'La fecha de fin debe ser posterior a la fecha de inicio.'
                )
            })

        # 2. Validar disponibilidad del espacio
        if self.espacio_id and not self.espacio.disponible:
            raise ValidationError({
                'espacio': 'Este espacio no se encuentra disponible para reservar.'
            })

        # 3. Validar solapamiento de horarios en el mismo espacio
        if self.espacio_id and self.fecha_inicio and self.fecha_fin:
            reservas_solapadas = Reserva.objects.filter(
                espacio=self.espacio,
                estado='confirmada',
                fecha_inicio__lt=self.fecha_fin,
                fecha_fin__gt=self.fecha_inicio,
            )

            # Excluir la reserva actual si se está editando
            if self.pk:
                reservas_solapadas = reservas_solapadas.exclude(pk=self.pk)

            if reservas_solapadas.exists():
                raise ValidationError({
                    'espacio': (
                        'El espacio ya está reservado en el horario'
                        ' seleccionado.'
                    )
                })

    def __str__(self):
        return f'Reserva #{self.pk} - {self.cliente.nombre} en {self.espacio.nombre}'