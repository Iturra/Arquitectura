from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.views.generic.edit import FormView

from Apps.ventaproducto.forms import AgregarPedido,AgregarPedidoEspecial
from Apps.ventaproducto.models import Pedido,Pedidoespecial
# Create your views here.

def index(request):
	return render(request, 'ventaproducto/index.html')




class VentaNormalCreate(CreateView):
	model = Pedido
	form_class = AgregarPedido
	template_name = 'ventaproducto/agregar_venta.html'
	success_url = reverse_lazy('ventaproducto:index')

class VentaEspecialCreate(CreateView):
	model = Pedidoespecial
	form_class = AgregarPedidoEspecial
	template_name = 'ventaproducto/agregar_venta.html'
	success_url = reverse_lazy('ventaproducto:index')
