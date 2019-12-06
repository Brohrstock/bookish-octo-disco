#renderizar cualquier template que creemos
from django.shortcuts import render, redirect

#para desplegar mensajes
from django.contrib import messages

#formas de autenticar y login de django
from django.contrib.auth import authenticate, login, logout

#redireccion a paginas mediante string
from django.http import HttpResponseRedirect, HttpResponse

#llamar urls usando el nombre de la url
from django.urls import reverse

#los forms que creamos en forms.py
from .forms import RegistrarForm

#los modelos que necesitemos
from .models import Noticia, Usuario

#redireccion a index despues de hacer logout
def logout_usuario(request):
    logout(request)
    return HttpResponseRedirect(reverse('Smash:index'))

#pagina principal
def index(request):
    return render(request, 'Smash/index.html', {})

#pagina de la galeria
def galeria(request):
    return render(request, 'Smash/galeria.html', {})

#pagina de contacto
def contacto(request):
    return render(request, 'Smash/contacto.html', {})

#Login usuario
def login_usuario(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('Smash:index'))
    else:
        if request.method == 'POST':
            #obtener campos desde el formulario y los asigno a las variables username y password
            username = request.POST.get('username')
            password = request.POST.get('password')
            #y lo autenticamos, si es que funciona devuelve el objeto y si no lo devuelve vacio
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('Smash:index'))
                else:
                    return HttpResponse("Tu cuenta esta inactiva")
            else:
                return HttpResponse("Datos invalidos")
        else:
            return render(request, 'Smash/login.html')

#Registrar usuario
def registrar(request):
    registrado = False
    if request.method == 'POST':
        #Obtengo la informacion desde el formulario y la paso a las variables user_form
        user_form = RegistrarForm(data=request.POST)
        if user_form.is_valid():
            #user_form.save lo guarda directamente en la base de datos
            usuario = user_form.save(commit=False)
            #Y si es que existe la imagen se le asigna al usuario
            if 'imagen' in request.FILES:
                usuario.foto_perfil = request.FILES['imagen']
            usuario.save()
            registrado = True
        else:
            return HttpResponse("Datos invalidos")
    else:
        user_form = RegistrarForm()

    return render(request, 'Smash/registrar.html',
        {'user_form': user_form,
         'registrado': registrado})


#Crud noticias juegos
#Listar Noticias
def listar_noticias(request):
    noticias = Noticia.objects.all()
    return render(request, 'Smash/listar_noticias.html', {'noticias':noticias})

#Eliminar Noticias
def eliminar_noticia(request, id):
    noticia = Noticia.objects.get(id=id)

    try:
        noticia.delete()
        mensaje = "Eliminado correctamente"
        messages.success(request, mensaje)
    except:
        mensaje = "Error al eliminar"
        messages.error(request, mensaje)

    return redirect('Smash:listar_noticias')