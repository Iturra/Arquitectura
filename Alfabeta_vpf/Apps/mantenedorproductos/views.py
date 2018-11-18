from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.views.generic.edit import FormView

from Apps.mantenedorproductos.forms import ProductoForm
from Apps.mantenedorproductos.models import Producto
# Create your views here.

def index(request):
	return render(request, 'mantenedor/index.html')

# Vista de cliente para adoptar un perrito  :3



class ProductoList(ListView):
	model = Producto
	template_name = 'mantenedor/listar_Producto.html'
	paginate_by = 3

class ProductoCreate(CreateView):
	model = Producto
	form_class = ProductoForm
	template_name = 'mantenedor/agregar_Producto.html'
	success_url = reverse_lazy('mantenedor:listar_Producto')

class ProductoUpdate(UpdateView):
	model = Producto
	form_class = ProductoForm
	template_name = 'mantenedor/modificar_Producto.html'
	success_url = reverse_lazy('mantenedor:listar_Producto')

class ProductoDelete(DeleteView):
	model = Producto
	template_name = 'mantenedor/eliminar_Producto.html'
	success_url = reverse_lazy('mantenedor:listar_Producto')

class ProductoSearch(TemplateView):
	def post(self, request, *args, **kwargs):
		buscar = request.POST['buscando']
		Producto = Producto.objects.filter(nombre=buscar)
		return render(request, 'mantenedor/buscar_Producto.html', {'Producto':Producto})
