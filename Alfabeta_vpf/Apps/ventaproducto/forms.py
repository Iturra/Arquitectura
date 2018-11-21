from django import forms
from Apps.mantenedorproductos.models import Producto
from Apps.ventaproducto.models import Pedido,Pedidoespecial

from django.db import models
from django.forms import ModelForm

class AgregarPedido(forms.Form):
    	class Meta:
    		model = Pedido

    		fields = [
    			"producto",
    			"cantidad",
    			"pagar",
    			#"username",
    		]
    		labels = {
    			'producto': 'producto',
    			'cantidad': 'cantidad',
    			'pagar': 'pagar',
    			#'username': 'username',
    		}
    		widgets = {
    			'producto': forms.ModelMultipleChoiceField(queryset=Producto.objects.all()),
    			'cantidad': forms.NumberInput(attrs={'class':'form-control'}),
    			'pagar': forms.NumberInput(attrs={'class':'form-control'}),
    			#'username': forms.User(attrs={'class':'form-control'}),
    		}

rellenos=(
('Manjar','Manjar'),
('Mermelada','Mermelada'),
('Sin Relleno','Sin Relleno'),
)

galletas=(
('Vainilla','Vainilla'),
('Coco','Coco'),
('Chocolate','Chocolate'),
)

coberturas=(
('Chocolate','Chocolate'),
('Chocolate Blanco','Chocolate Blanco'),
('Sin Cobertura','Sin Cobertura'),
)

figuras=(
('Corazon','Corazon'),
('Flor','Flor'),
('Calavera','Calavera'),
('Sin figuras','Sin figuras'),
)

class AgregarPedidoEspecial(forms.Form):
    	class Meta:
    		model = Pedidoespecial

    		fields = [
    			"relleno",
    			"galleta",
    			"cobertura",
                "figura",
                "cantidad",
    			#"username",
    		]
    		labels = {
    			'relleno': 'relleno',
    			'galleta': 'galleta',
                'cobertura': 'cobertura',
                'figura': 'figura',
                'cantidad': 'cantidad',
    			#'username': 'username',
    		}
    		widgets = {
    			'relleno': forms.ChoiceField(choices=rellenos),
    			'galleta': forms.ChoiceField(choices=galletas),
                'cobertura': forms.ChoiceField(choices=coberturas),
                'figura': forms.ChoiceField(choices=figuras),
    			'cantidad': forms.NumberInput(attrs={'class':'form-control'}),
    			#'username': forms.User(attrs={'class':'form-control'}),
    		}
