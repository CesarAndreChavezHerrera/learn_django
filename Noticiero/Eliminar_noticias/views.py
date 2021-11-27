from django.shortcuts import render
from Portada import models
# Create your views here.
def eliminar_noticia(r):
    if r.method == "POST":
        id_noticia = r.POST.get("id",None)
        borrar = models.Noticia_db.objects.get(id = id_noticia)
        borrar.delete()
        pass
    noticias = models.Noticia_db.objects.all()
    return render(r,"eliminar_noticia.html",{"noticias":noticias})
    pass