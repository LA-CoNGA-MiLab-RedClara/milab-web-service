from django.shortcuts import render, HttpResponse
#from serviciosApp.models import Servicio
from mainApp.models import Servicio, Noticia, Recurso

# Create your views here.

def inicio (request):
    #    return HttpResponse("Inicio")
    return render(request,"mainApp/inicio.html")

def acerca (request):
    return render(request,"mainApp/acerca.html")

def servicios (request):
    servicios = Servicio.objects.all()
#    return render(request,"servicios/servicios.html", {"servicios": servicios})
    return render(request,"mainApp/servicios.html", {"servicios": servicios})

def noticias (request):
    noticias = Noticia.objects.all()
    return render(request,"mainApp/noticias.html", {"noticias": noticias})

def recursos (request):
    recursos = Recurso.objects.all()
    return render(request,"mainApp/recursos.html", {"recursos": recursos})

def contacto (request):
#    return HttpResponse("Contacto")
    return render(request,"mainApp/contacto.html")

