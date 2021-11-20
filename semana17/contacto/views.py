from django.shortcuts import render
from contacto import models

def contacto_pagina(r):
    if r.method=="POST":
        recibirnombre = r.POST.get("nombre", None)
        recibirtema = r.POST.get("tema", None)
        recibirpregunta = r.POST.get("pregunta", None)

        models.Contacto.objects.create(
            nombre = recibirnombre,
            tema = recibirtema,
            pregunta = recibirpregunta)
    
    c = models.Contacto.objects.all()
    return render(r,"contacto.html",{"consulta":c})
