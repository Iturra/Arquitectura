from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from Apps.ventaproducto import views

urlpatterns = [
url(r'^$', views.index, name='index'),
url(r'^CompraNormal$', views.VentaNormalCreate.as_view(), name='CompraNormal'),
url(r'^CompraEspecial$', views.VentaEspecialCreate.as_view(), name='CompraEspecial'),

]
