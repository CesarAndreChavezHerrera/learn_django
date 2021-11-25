from django.shortcuts import render
from Ingreso import models

# Create your views here.
def mostrar_datos(r):
    consulta = models.Ingreso_bd.objects.all()
    
    return render(r,"datos.html",{"consulta":consulta})
    pass