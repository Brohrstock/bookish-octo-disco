#Imports necesarios de nuestro proyecto
from django import forms
from django.contrib.auth.models import User
from .models import Noticia, Usuario

#Form para el registro de usuarios
class RegistrarForm(forms.ModelForm):
    clave = forms.CharField(widget=forms.PasswordInput(), label='Contraseña')
    class Meta:
        model = Usuario
        fields = ('nombre_usuario', 'clave', 'nombre_completo', 'estado_actual', 'cargo', 'imagen')

        #Remplazar los nombres de los fields con las labels que queramos
        labels = {
            'nombre_usuario' : 'Nombre de Usuario',
            'nombre_completo' : 'Nombre Completo',
            'clave' : 'Contraseña',
            'estado_actual' : 'Estado Actual',
            'cargo' : 'Cargo',
            'imagen' : 'Foto de Perfil'
        }

        #Ingresar textos de ayuda para llenado
        help_texts = {
            'nombre_usuario' : '',
        }

        #mensajes de error
        error_messages = {
            'nombre_usuario' : {
                'max_length': 'Maximo 150 caracteres',
                'required': 'Requerido'
            },
            'clave' : {
                'required': 'Requerido'
            },
        }

    #Constructor del formulario , le cambiamos la clase a form-control
    def __init__(self, *args, **kwargs):
        super(RegistrarForm, self).__init__(*args, **kwargs)
        self.fields['nombre_usuario'].widget.attrs.update({'class': 'form-control'})
        self.fields['nombre_completo'].widget.attrs.update({'class': 'form-control'})
        self.fields['clave'].widget.attrs.update({'class': 'form-control'})
        self.fields['estado_actual'].widget.attrs.update({'class': 'form-control'})
        self.fields['cargo'].widget.attrs.update({'class': 'form-control'})
        
