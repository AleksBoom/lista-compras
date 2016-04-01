from django.db import models
from django.utils import timezone

class Producto(models.Model):
    nombre=models.CharField(max_length=200)
    fechaRegistroInicial=models.DateTimeField()
    fechaCompra=models.DateTimeField(blank=True, null=True)


    def comprar(self):
        self.fechaCompra=timezone.now()
        self.save()

    def __str__(self):
        return self.nombre
