from django.conf.urls import url
from Apps.mantenedorproductos import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^agregar$', views.ProductoCreate.as_view(), name='agregar_Producto'),
    url(r'^listar', views.ProductoList.as_view(), name='listar_Producto'),
    url(r'^modificar/(?P<pk>\d+)/$', views.ProductoUpdate.as_view(), name='actualizar_Producto'),
    url(r'^eliminar/(?P<pk>\d+)/$', views.ProductoDelete.as_view(), name='eliminar_Producto'),
    url(r'^buscar$', views.ProductoSearch.as_view(), name='buscar_Producto'),

]
