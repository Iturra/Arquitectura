from django import forms
from Apps.mantenedorproductos.models import *
from Apps.ventaproducto.models import *

from django.db import models
from django.forms import ModelForm

rellenos=(
(1,"Manjar"),
(2,"Mermelada"),
(3,"Sin Relleno"),
)

galletas=(
(1,"Vainilla"),
(2,"Coco"),
(3,"Chocolate"),
)

coberturas=(
(1,"Chocolate"),
(2,"Chocolate Blanco"),
(3,"Sin Cobertura"),
)

figuras=(
(1,"Corazon"),
(2,"Flor"),
(3,"Calavera"),
(4,"Sin figuras"),
)

class AgregarVentaNormalForm(forms.ModelForm):
	class Meta:
		model = Pedido

		fields = [
			"producto",
			"cantidad",
			"pagar",

		]
		labels = {
			'producto': 'Seleccione el producto a comprar',
			'cantidad': 'Ingrese la cantidad a comprar',
			'pagar': 'pagar',

		}
		widgets = {
            'producto': forms.Select(attrs={'class':'form-control'}),
			'cantidad': forms.NumberInput(attrs={'class':'form-control'}),
			'pagar': forms.NumberInput(attrs={'class':'form-control'}),

		}


class AgregarVentaNormal(forms.Form):
    producto=forms.ModelChoiceField(queryset=Producto.objects.all())
    cantidad=forms.IntegerField()
    pagar=forms.IntegerField()

class AgregarVentaEspecial(forms.Form):

    relleno = forms.ChoiceField(choices=rellenos)
    galleta = forms.ChoiceField(choices=galletas)
    cobertura = forms.ChoiceField(choices=coberturas)
    figura = forms.ChoiceField(choices=figuras)
    cantidad = forms.IntegerField()
