from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate
from Apps.ventaproducto.forms import *
from Apps.ventaproducto.models import *
# Create your views here.

def index(request):
	return render(request, 'ventaproducto/index.html')

def agregarpedidonormal(request):
     form=AgregarVentaNormal(request.POST)
     if form.is_valid():
         data=form.cleaned_data
         pedidos=Pedido(data.get("producto"),data.get("cantidad"),data.get("pagar"))

         pedidos.save()


     form=AgregarVentaNormal()
     return render(request,"ventaproducto/agregar_ventanormal.html",{'form':form,'Pedido':Pedido,})

def agregarpedidoespecial(request):
     form=AgregarVentaEspecial(request.POST)
     if form.is_valid():
         data=form.cleaned_data
         pedidos=Pedidoespecial(data.get("relleno"),data.get("galleta"),data.get("cobertura"),data.get("figura"),data.get("cantidad"))
         pedidos.save()
     form=AgregarVentaEspecial()
     return render(request,"ventaproducto/agregar_ventaespecial.html",{'form':form,'Pedidoespecial':Pedidoespecial,})
