from django.db import models

from django.core.exceptions import ValidationError
from django.db import models



class Cliente(models.Model):
    nombre = models.CharField(max_length=100) 
    dni = models.CharField(max_length=10, unique=True)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)

    def cliente(self):
        super().clean()
        # Valida que el dni contenga solo numeros.
        if self.dni and not self.dni.isdigit():
            raise ValidationError({'dni': "El dni debe contener solo numero."})

    def __str__(self):
        return f"{self.nombre}, ({self.dni})"
