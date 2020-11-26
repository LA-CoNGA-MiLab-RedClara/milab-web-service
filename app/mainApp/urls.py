from django.urls import path

from mainApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.inicio, name="Inicio"),     
    path('registro', views.registro, name="Registro"),     
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)