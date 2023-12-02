from django.db import models

# Create your models here.

class Vuelo(models.Model):
    Origen = models.CharField(max_length=64)
    Destino = models.CharField(max_length=64)
    Duracion = models.IntegerField()

class Aeropuerto(models.Model):
    codigo = models.CharField(max_length=3)
    ciudad = models.CharField(max_length=250)

def __str__(self):
    return f"{self.id} - {self.Origen} Hacia {self.Destino} "