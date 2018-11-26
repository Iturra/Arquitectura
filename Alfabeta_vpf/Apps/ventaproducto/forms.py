from django import forms
from Apps.mantenedorproductos.models import *
from Apps.ventaproducto.models import *

from django.db import models
from django.forms import ModelForm

rellenos=(
("Manjar","Manjar"),
("Mermelada","Mermelada"),
("Sin Relleno","Sin Relleno"),
)

galletas=(
("Vainilla","Vainilla"),
("Coco","Coco"),
("Chocolate","Chocolate"),
)

coberturas=(
("Chocolate","Chocolate"),
("Chocolate Blanco","Chocolate Blanco"),
("Sin Cobertura","Sin Cobertura"),
)

figuras=(
("Corazon","Corazon"),
("Flor","Flor"),
("Calavera","Calavera"),
("Sin figuras","Sin figuras"),
)

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
