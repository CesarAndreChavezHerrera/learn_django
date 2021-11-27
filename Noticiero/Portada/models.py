from django.db import models
from django.db.models.base import Model
from django.utils import timezone
# Create your models here.
class Noticia_db (models.Model):

    nombre = models.CharField(max_length=100)
    tema = models.CharField(max_length=500)
    contenido = models.TextField()
    fecha = models.TimeField(default=timezone.now)

    def __str__(self):
        return self.tema

    pass