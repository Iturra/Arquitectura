from django.contrib import admin

# Register your models here.
from Apps.mantenedorproductos.models import *
from Apps.ventaproducto.models import *
# Register your models here.
admin.site.register(Producto)
admin.site.register(Pedido)
admin.site.register(Pedidoespecial)
