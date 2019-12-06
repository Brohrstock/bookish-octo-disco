#Imports necesarios de nuestro proyecto
from django.contrib import admin
from .models import PerfilUsuario, Image, Usuario, Noticia

#Personalizar la cantidad de informacion que despliega al listar usuarios 
#Agregar funcion de busqueda "search_fields" y definir sus campos 
#Agregar funcion de filtro "list_filter" y definir sus campos
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre_usuario', 'nombre_completo', 'estado_actual', 'cargo')
    search_fields = ['nombre_usuario', 'cargo']
    list_filter = ('estado_actual', 'cargo')

class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo_noticia', 'descripcion')
    search_fields = ['titulo_noticia']

# Modelos que queremos registrar en nuestra base de datos y las modificaciones que agregemos en admin.py (Ejemplo Usuario le agregamos UsuarioAdmin)
# Que es la clase que usamos para personalizar como se muestra
admin.site.register(PerfilUsuario)
admin.site.register(Image)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Noticia, NoticiaAdmin)