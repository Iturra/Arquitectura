from django.conf.urls import url
from Apps.ventaproducto import views

urlpatterns = [
url(r'^$', views.index, name='index'),
url(r'^CompraNormal', views.agregarpedidonormal, name='CompraNormal'),
url(r'^CompraEspecial', views.agregarpedidoespecial, name='CompraEspecial'),

]
