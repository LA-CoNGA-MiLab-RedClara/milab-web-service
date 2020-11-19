from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
#from serviciosApp.models import Servicio
from mainApp.models import Servicio, Noticia, Recurso

# Create your views here.

@login_required
def inicio (request):
    #    return HttpResponse("Inicio")
    return render(request,"mainApp/inicio.html")

@login_required
def acerca (request):
    return render(request,"mainApp/acerca.html")

@login_required
def servicios (request):
    servicios = Servicio.objects.all()
#    return render(request,"servicios/servicios.html", {"servicios": servicios})
    return render(request,"mainApp/servicios.html", {"servicios": servicios})

@login_required
def noticias (request):
    noticias = Noticia.objects.all()
    return render(request,"mainApp/noticias.html", {"noticias": noticias})

@login_required
def recursos (request):
    recursos = Recurso.objects.all()
    return render(request,"mainApp/recursos.html", {"recursos": recursos})

@login_required
def contacto (request):
#    return HttpResponse("Contacto")
    return render(request,"mainApp/contacto.html")

