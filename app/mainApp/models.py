from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

class Servicio(models.Model):
    titulo = models.CharField(max_length=200) 
    descripcion = RichTextField(blank=True, null=True)
    imagen = models.ImageField(upload_to='servicios')
    enlace = models.CharField(max_length=400)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'
    
    def __str__(self):
        return self.titulo
    
class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
        
    class Meta:
        verbose_name = 'Categoria para noticias'
        verbose_name_plural = 'Categorias para noticias'
        
    def __str__(self):
        return self.nombre
    
    
class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = RichTextField(blank=True, null=True)
    imagen = models.ImageField(upload_to='noticias', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    categorias = models.ManyToManyField(Categoria)
    
    class Meta:
        verbose_name = 'noticia'
        verbose_name_plural = 'noticias'
        
    def __str__(self):
        return self.titulo

class CategoriaRecurso(models.Model):
    nombre = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
        
    class Meta:
        verbose_name = 'Categoria para recurso'
        verbose_name_plural = 'Categorias para recursos'
        
    def __str__(self):
        return self.nombre

class Recurso(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    archivo = models.FileField(upload_to='recursos', null=True)
    estado = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    categorias = models.ManyToManyField(CategoriaRecurso)
    
    class Meta:
        verbose_name = 'recurso'
        verbose_name_plural = 'recursos'
        
    def __str__(self):
        return self.titulo

class Contacto(models.Model):
    asunto = models.CharField(max_length=100)
    mensaje = models.TextField(null=False)
    remitente = models.CharField(max_length=100)
    email = models.EmailField()

    class Meta:
        verbose_name = 'contacto'
        verbose_name_plural = 'contactos'

    def __str__(self):
        return self.asunto

