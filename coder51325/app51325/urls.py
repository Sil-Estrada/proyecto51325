from django.urls import path
from .views import *



urlpatterns= [

    path('proveedor/',proveedores_ ),
    path('cliente/',cliente_ ),
    path('producto/',producto_ ),
    path('carrito/',carrito_ ),
    path('alta_proveedor/',alta_proveedor ),




]