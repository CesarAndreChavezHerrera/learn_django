from django.db import models
from django.utils import timezone
# Create your models here.
class Contacto(models.Model):
    nombre = models.CharField(max_length=200)
    tema = models.CharField(max_length=200)
    pregunta= models.TextField()
    fecha = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.tema