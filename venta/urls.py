from django.urls import path
from .views import index
import venta.cliente.views  as cliente
import venta.producto.views  as producto
import venta.venta.views  as venta

urlpatterns = [
    path(route = '',view =index, name = 'home'),
    path(route = 'clientes/',view =cliente.Index.as_view(), name = 'cliente.index'),
    path(route = 'clientes/create',view =cliente.Create.as_view(), name = 'cliente.store'),
    path(route = 'clientes/edit/<pk>',view =cliente.Update.as_view(), name = 'cliente.update'),
    path(route = 'clientes/delete/<pk>',view =cliente.Delete.as_view(), name = 'cliente.delete'),
        
    path(route = 'productos/',view =producto.Index.as_view(), name = 'producto.index'),
    path(route = 'productos/create',view =producto.Create.as_view(), name = 'producto.store'),
    path(route = 'productos/edit/<pk>',view =producto.Update.as_view(), name = 'producto.update'),
    path(route = 'productos/delete/<pk>',view =producto.Delete.as_view(), name = 'producto.delete'),
    
    path(route = 'ventas/',view =venta.Index.as_view(), name = 'venta.index'),
    path(route = 'ventas/create',view =venta.Create.as_view(), name = 'venta.store'),
    path(route = 'ventas/edit/<pk>',view =venta.Update.as_view(), name = 'venta.update'),
    path(route = 'ventas/delete/<pk>',view =venta.Delete.as_view(), name = 'venta.delete'),

]