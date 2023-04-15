from django.http import HttpResponse
import datetime
from django.template import Template, Context

def saludar(request):
    return HttpResponse("Hola Mundo!!!!!!!!!!")

def chau(request):
    return HttpResponse("Vuelvan prontos")

def dia_de_hoy(request):
    dia = datetime.datetime.today()
    dia_texto = f"hoy es {dia}"
    return HttpResponse(dia_texto)

def saludo_nombre(request, nombre):
    return HttpResponse(f'Saludirijillos {nombre} como estas hoy')

def cal_anio_nac(request, edad):
    anio_actual = datetime.datetime.today().year
    anio_nac = anio_actual-int(edad)    
    return HttpResponse(f'Usted nacio aprox en el año {anio_nac}')


def prob_html(request):

    archivo = open(r"C:\Users\Silvano Estrada\Desktop\CURSOS\CODER - PYTHON\Trabajo51325\Plantillas\template1.html")
    #texto = archivo.read()
    

    temp = Template(archivo.read())

    archivo.close()
    cont = Context()
    doc = temp.render(cont)

    return HttpResponse(doc)
