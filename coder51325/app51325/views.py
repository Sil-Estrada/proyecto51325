from django.shortcuts import render
from .models import proveedor
from django.http import HttpResponse


def alta_proveedor (request):

    nomb_prov = "Duff"
    dire = "Avenida Siempre Viva 3000"
    cuit_ = int(123456789)
    tel_ = int(555667788)

    prov = proveedor(provee_nombre=nomb_prov, direccion=dire, cuit=cuit_, telefono=tel_)
    prov.save()

    respuesta = f"Alta Exitosa del cliente {nomb_prov}"

    return HttpResponse(respuesta)

def proveedores_ (request):
    return render(request, 'proveedores.html')

def cliente_ (request):
    return render(request, 'clientes.html')

def producto_ (request):
    return render(request, 'productos.html')

def carrito_ (request):
    return render(request, 'carrito.html')

def inicio(request):
    return render(request, 'inicio.html')










# Create your views here.
