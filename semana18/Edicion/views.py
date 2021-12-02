from django.shortcuts import render
from Ingreso import models

# Create your views here.
def mostrar_datos(r):
    
    if r.method == "POST":
        
        accion = r.POST.get("accion",None)
       
        if accion =="eliminar":
            

            #return render(r,"test_1.html")
            id_consulta = r.POST.get("id",None)
            borrar = models.Ingreso_bd.objects.get(id = id_consulta)
            borrar.delete()
        elif accion =="modificar":
            id_consulta = r.POST.get("id",None)
            modificar = models.Ingreso_bd.objects.get(id = id_consulta)
            return render(r,"datos_modificar.html",{"consulta":modificar})

        elif accion == "guardar_cambio":
            
            id_consulta = r.POST.get("id",None)
            m_nombre = r.POST.get("nombre")
            m_tema = r.POST.get("tema")
            m_pregunta = r.POST.get("pregunta")

            modificar = models.Ingreso_bd.objects.get(id = id_consulta)
            
            modificar.nombre = m_nombre
            modificar.tema = m_tema
            modificar.pregunta = m_pregunta
            modificar.save()

            
            
            pass

        """
        try:

            id_consulta = r.POST.get("id_a_eliminar")
            
            pass
        except:
            id_consulta = r.POST.get("id_a_modificar")
            return render(r,"test_2.html")
            pass
        """
        pass
    consulta = models.Ingreso_bd.objects.all()
    return render(r,"datos.html",{"consulta":consulta})
    pass