from django.http import request
from django.shortcuts import render
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required

from mainApp.models import Servicio
from mainApp.models import Noticia
from mainApp.models import Recurso

from mainApp.forms import FormularioContacto

@login_required
def inicio (request):
    servicios = Servicio.objects.all()
    noticias = Noticia.objects.all()
    recursos = Recurso.objects.all()
    contacto = FormularioContacto()
    return render(
                request,
                "mainApp/index.html",
                {
                    "servicios": servicios,
                    "noticias": noticias,
                    "recursos": recursos,
                    "contacto": contacto,
                }
            )

@login_required
def registro (request):
    contacto = FormularioContacto(request.POST)
    servicios = Servicio.objects.all()
    noticias = Noticia.objects.all()
    recursos = Recurso.objects.all()
    if contacto.is_valid():
        contacto.save()
        contacto = FormularioContacto()

    return render (
                request,
                "mainApp/index.html",
                {
                    "servicios": servicios,
                    "noticias": noticias,
                    "recursos": recursos,
                    "contacto": contacto,
                    "mensaje": "OK",
                }
        )
