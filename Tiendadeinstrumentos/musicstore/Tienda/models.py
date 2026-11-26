from django.db import models


class Instrumento(models.Model):

    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)
    descripcion = models.TextField()

    precio = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    precio_anterior = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )

    descuento = models.IntegerField(default=0)

    imagen = models.URLField(blank=True)

    def __str__(self):
        return self.nombre
