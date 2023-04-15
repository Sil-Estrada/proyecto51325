from django.http import HttpResponse
import datetime
from django.template import Template, Context, loader


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
    
    dic = {"Nombre":"Homero", "Apellido":"Simpson", "Cliente":"1"}


    temp = Template(archivo.read())

    archivo.close()
    cont = Context(dic)
    doc = temp.render(cont)

    return HttpResponse(doc)


def probloaderhtml(request):

    diccionario= {"Nombre":"Homero", "Apellido":"Simpson", "Cliente":"1", "DNI":"C4204123"}

    template = loader.get_template('template1.html')

    documento = template.render(diccionario)

    return HttpResponse(documento)
