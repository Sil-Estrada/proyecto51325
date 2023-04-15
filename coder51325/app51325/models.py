from django.db import models

class cliente(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    dni = models.IntegerField()
    nombre = models.EmailField()

class proveedor(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    cuit = models.CharField(max_length=11)
    telefono = models.IntegerField()

class producto(models.Model):
    nombre = models.CharField(max_length=15)
    rubro = models.CharField(max_length=10)
    precio = models.FloatField()
    nom_proveedor = models.CharField(max_length=30)
    


# Create your models here.
