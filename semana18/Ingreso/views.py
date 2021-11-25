from django.shortcuts import render
from Ingreso import models

# Create your views here.
def ingreso_datos(r):
    if r.method == "POST":
        r_nombre = r.POST.get("nombre")
        r_tema = r.POST.get("tema")
        r_pregunta = r.POST.get("pregunta")

        if r_nombre != "":
            if r_pregunta != "":
                if r_tema !="":
                    models.Ingreso_bd.objects.create(
                        nombre = r_nombre,
                        tema = r_tema,
                        pregunta = r_pregunta
            )
            #print("falta nombre")
    return render(r,"catura.html")
    pass