from django.shortcuts import render
from . import models
# Create your views here.
def portada(r):
    
    noticias = models.Noticia_db.objects.all()
    return render(r,"noticia.html",{"noticia":noticias})
    pass