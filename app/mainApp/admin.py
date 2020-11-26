from django.contrib import admin

# Register your models here.

from mainApp.models import Servicio
from mainApp.models import Categoria
from mainApp.models import Noticia
from mainApp.models import CategoriaRecurso
from mainApp.models import Recurso
from mainApp.models import Contacto

class ServicioAdmin (admin.ModelAdmin):
    readonly_fields=('created','updated')

class CategoriaAdmin (admin.ModelAdmin):
    readonly_fields=('created', 'updated') 
    
class NoticiaAdmin (admin.ModelAdmin):
    readonly_fields=('created', 'updated') 
    
class CategoriaRecursoAdmin (admin.ModelAdmin):
    readonly_fields=('created', 'updated')

class RecursoAdmin (admin.ModelAdmin):
    readonly_fields=('created', 'updated')

class ContactoAdmin (admin.ModelAdmin):
    readonly_fields=()

admin.site.register(Servicio, ServicioAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Noticia, NoticiaAdmin)
admin.site.register(CategoriaRecurso, CategoriaRecursoAdmin)
admin.site.register(Recurso, RecursoAdmin)
admin.site.register(Contacto, ContactoAdmin)
