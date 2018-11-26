from django.db import models
from Apps.mantenedorproductos.models import Producto
from django.forms import ModelForm
# Create your models here.
class Pedido(models.Model):
    producto = models.OneToOneField(Producto,blank=True,on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    pagar = models.IntegerField()

class Pedidoespecial(models.Model):

    relleno = models.CharField(max_length=40)
    galleta = models.CharField(max_length=40)
    cobertura = models.CharField(max_length=40)
    figura = models.CharField(max_length=40)
    cantidad = models.IntegerField()
