from django import forms

from Apps.mantenedorproductos.models import Producto

class ProductoForm(forms.ModelForm):
	class Meta:
		model = Producto

		fields = [
			"nombre",
			"precio",
			"descripcion",
			"fotografia",
		]
		labels = {
			'nombre': 'Nombre',
			'precio': 'Precio',
			'descripcion': 'Descripcion',
			'fotografia': 'Sube la foto del Producto',
		}
		widgets = {
			'fotografia': forms.FileInput(attrs={'class':'form-control'}),
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'precio': forms.TextInput(attrs={'class':'form-control'}),
			'descripcion': forms.TextInput(attrs={'class':'form-control'}),
		}
