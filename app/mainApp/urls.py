from django.urls import path

from mainApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.inicio, name="Inicio"), 
    path('acerca', views.acerca, name="Acerca"), 
    path('servicios', views.servicios, name="Servicios"),
    path('noticias', views.noticias, name="Noticias"),
    path('recursos', views.recursos, name="Recursos"),
    path('contacto', views.contacto, name="Contacto"),
    
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)