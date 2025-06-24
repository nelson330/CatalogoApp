from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=70, verbose_name="nombre")
    descripcion = models.TextField(verbose_name="Descripcion")
    stock = models.IntegerField(default=0, verbose_name="Unidades")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="fecha")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"



# Create your models here.
