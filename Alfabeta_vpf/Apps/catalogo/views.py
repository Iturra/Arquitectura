from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.views.generic.edit import FormView

from Apps.mantenedorproductos.forms import ProductoForm
from Apps.mantenedorproductos.models import Producto

# Create your views here.
def index(request):
	return render(request, 'catalogo/index.html')

class ProductoList(ListView):
	model = Producto
	template_name = 'catalogo/vista2.html'
	paginate_by = 3
