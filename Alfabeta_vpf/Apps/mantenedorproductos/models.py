from django.db import models

# Create your models here.

class Producto(models.Model):
	fotografia = models.ImageField(upload_to='profile_pics/%Y-%m-%d/')
	nombre = models.CharField(max_length=50)
	precio = models.CharField(max_length=50)
	descripcion = models.CharField(max_length=70)
