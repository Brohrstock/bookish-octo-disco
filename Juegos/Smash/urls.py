from django.conf.urls import url
from django.urls import path

from . import views
app_name = 'Smash'

#Urls del proyecto y la vista correspondiente de donde esta el metodo de redireccion
urlpatterns = [
    url('registrar', views.registrar, name='registrar'),
    url('login', views.login_usuario, name='login'),
    url('logout', views.logout_usuario, name='logout'),
    url('galeria', views.galeria, name='galeria'),
    url('contacto', views.contacto, name='contacto'),
    url('listar_noticias', views.listar_noticias, name='listar_noticias'),
    path('eliminar_noticia/<id>/', views.eliminar_noticia, name='eliminar_noticia'),
    url('', views.index , name='index'),
]
