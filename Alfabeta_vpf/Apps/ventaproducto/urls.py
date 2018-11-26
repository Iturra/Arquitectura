from django.conf.urls import url
from Apps.ventaproducto import views

urlpatterns = [
url(r'^$', views.index, name='index'),
url(r'^CompraNormal', views.PedidoCreate.as_view(), name='CompraNormal'),
url(r'^CompraEspecial', views.agregarpedidoespecial, name='CompraEspecial'),
url(r'^mensaje', views.mensaje, name='mensaje'),
]
