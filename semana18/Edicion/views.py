from django.shortcuts import render
from Ingreso import models

# Create your views here.
def mostrar_datos(r):
    
    if r.method == "POST":
        id_consulta = r.POST.get("id",None)
        borrar = models.Ingreso_bd.objects.get(id = id_consulta)
        borrar.delete()
        pass
    consulta = models.Ingreso_bd.objects.all()
    return render(r,"datos.html",{"consulta":consulta})
    pass