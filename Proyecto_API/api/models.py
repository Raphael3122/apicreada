from django.db import models

# Create your models here.

class Registro(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.CharField(max_length=100)
    contrasena = models.CharField(max_length=20)