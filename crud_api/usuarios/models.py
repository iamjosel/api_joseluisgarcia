from django.db import models

class Usuario(models.Model):
    IdU = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=255)
    Telefono = models.CharField(max_length=15)
    Correo = models.EmailField(max_length=255)
    Ciudad = models.CharField(max_length=100)
    FechaIngreso = models.DateField()

    def __str__(self):
        return self.Nombre
