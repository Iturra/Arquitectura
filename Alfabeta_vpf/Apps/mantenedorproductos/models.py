from django.db import models

# Create your models here.

class Producto(models.Model):
	fotografia = models.ImageField(upload_to='profile_pics/%Y-%m-%d/')
	nombre = models.CharField(max_length=50)
	precio = models.IntegerField()
	descripcion = models.CharField(max_length=70)

	def __unicode__(self):
		return str(self.nombre)
