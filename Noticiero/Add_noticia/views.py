from django.shortcuts import render

from Portada import models
# Create your views he
def add_noticia(r):

    if r.method == "POST":
        r_nombre = r.POST.get("nombre")
        r_tema = r.POST.get("tema")
        r_contenido = r.POST.get("contenido")

        
        if r_nombre != "":
            if r_contenido != "":
                if r_tema !="":
                    models.Noticia_db.objects.create(
                        nombre = r_nombre,
                        tema = r_tema,
                        contenido = r_contenido
            )
        
    return render(r,"add_noticia.html")
    pass