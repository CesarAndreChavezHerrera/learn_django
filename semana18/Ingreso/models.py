from django.db import models

# Create your models here.

class Ingreso_bd(models.Model):

    nombre = models.CharField(max_length=100)
    tema = models.CharField(max_length=100)
    pregunta = models.TextField()

    def __str__(self):
        return self.nombre
    pass