from django.db import models
from Apps.mantenedorproductos.models import Producto
# Create your models here.
class Pedido(models.Model):
    producto = models.ManyToManyField(Producto)
    cantidad = models.IntegerField()
    Pagar = models.IntegerField()


class Pedidoespecial(models.Model):

    relleno = models.CharField(max_length=20)
    galleta = models.CharField(max_length=20)
    cobertura = models.CharField(max_length=20)
    figura = models.CharField(max_length=20)
    cantidad = models.IntegerField()
