from django.shortcuts import render
from Portada import models
# Create your views here.
def eliminar_noticia(r):
    if r.method == "POST":
        accion = r.POST.get("accion",None)
        if accion =="eliminar":
            
            #return render(r,"test_1.html")
            id_consulta = r.POST.get("id",None)
            borrar = models.Noticia_db.objects.get(id = id_consulta)
            borrar.delete()
        elif accion =="modificar":
            id_consulta = r.POST.get("id",None)
            modificar = models.Noticia_db.objects.get(id = id_consulta)
            return render(r,"datos_modificar.html",{"consulta":modificar})

        elif accion == "guardar_cambio":
            
            id_consulta = r.POST.get("id",None)
            m_nombre = r.POST.get("nombre")
            m_tema = r.POST.get("tema")
            m_contenido = r.POST.get("pregunta")

            modificar = models.Noticia_db.objects.get(id = id_consulta)
            
            modificar.nombre = m_nombre
            modificar.tema = m_tema
            modificar.contenido = m_contenido
            modificar.save()

            
            
            pass
        pass
    noticias = models.Noticia_db.objects.all()
    return render(r,"eliminar_noticia.html",{"noticias":noticias})
    pass