from django.urls import path
from .views import *



urlpatterns= [

    path('proveedor/',proveedores_, name= "proveedor"),
    path('cliente/',cliente_ , name = "cliente"),
    path('producto/',producto_, name ="producto" ),
    path('carrito/',carrito_ , name = "carrito"),
    path('alta_proveedor/',alta_proveedor, name = "AltaProveedor" ),
    path('alta_cliente/',alta_cliente, name ="AltaCliente" ),
    path('ofertas/',prod_oferta, name = "ofertas" ),




]