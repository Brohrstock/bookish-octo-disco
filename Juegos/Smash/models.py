from django.db import models
from django.contrib.auth.models import User
from django import forms

#Modelo antiguo para prueba que tenia foto y campos de autenticazion
class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    foto_perfil = models.ImageField(upload_to='foto_perfil', blank=True)

    def __str__(self):
        return self.user.username

#Modelo para subir las imagenes y mostrarlas en la galeria
class Image(models.Model):
    nombre = models.CharField(max_length=500)
    imagen = models.ImageField(upload_to='img', height_field=None, width_field=None)

    def __str__(self):
        return self.nombre

#Modelo nuevo para usuario segun rubrica
class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=50)
    clave = models.CharField(max_length=50)
    nombre_completo = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='foto_usuarios', blank=True)
    fecha_registro = models.DateField(auto_now_add=True)
    estado_actual = models.CharField(max_length=50)
    cargo = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_usuario

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

#Modelo para las noticias que se despliegan en listar_noticias
class Noticia(models.Model):
    titulo_noticia = models.CharField(max_length=50) 
    descripcion = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.titulo_noticia
