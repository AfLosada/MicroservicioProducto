from django.db import models

# Create your models here.

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    precio = models.DecimalField(decimal_places=5, max_digits=10)
    cantidad = models.PositiveIntegerField(null=False, blank=False)

    def __str__(self):
        cadena = "{0}    Precio:{1}    cantidad:{2}"
        return cadena.format(self.nombre, self.precio, self.cantidad)