from django.conf.urls import url
from Apps.catalogo.views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^vista2', ProductoList.as_view(), name='vista2'),


]
