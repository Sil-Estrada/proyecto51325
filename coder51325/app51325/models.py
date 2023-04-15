from django.db import models

class cliente(models.Model):
    cli_nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    dni = models.IntegerField()
    mail = models.EmailField()

class proveedor(models.Model):
    provee_nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    cuit = models.CharField(max_length=11)
    telefono = models.IntegerField()

class producto(models.Model):
    cod_prod= models.IntegerField()
    nombre = models.CharField(max_length=15)
    rubro = models.CharField(max_length=10)
    precio = models.FloatField()
    nom_proveedor = models.CharField(max_length=30)

class carrito(models.Model):
    cli_nombre = models.CharField(max_length=20)
    cod_prod= models.IntegerField()
    nombre = models.CharField(max_length=15)
    cantidad_unidades = models.IntegerField()


    


    


# Create your models here.
