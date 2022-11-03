from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

# Tabla Producto

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()
    marca = models.CharField(max_length=50)
    fecha_registro = models.DateField()
    fecha_vencimiento = models.DateField()

def __str__(self):
    return self.nombre;

# Tabla Cliente

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    mail = models.CharField(max_length=50)

def __str__(self):
    return self.nombre;
    

