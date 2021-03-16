from django.urls import path
from .views import home, listaRep , Administracion, Crearcancion, CrearAutor, CrearCancionConGenero, pop, alternativo, rock, registro, inicio, delete
urlpatterns = [
path('', inicio , name='benido'),
path ('inicio/', home , name='homes'),
path ('pop/', pop , name='pop'),
path ('rock/', rock , name='rock'),
path ('alternativa/', alternativo , name='alternativo'),
path ('lista/', listaRep , name='listarep'),
path('Adminitracion/',Administracion, name='administracion'),
path('registro/',registro, name='registro'),

#MODALES CREACION
path('Crearcancion/', Crearcancion, name='mod2'),
path('CrearAutor/', CrearAutor, name='mod'),
path('CreaCancionConGenero/' , CrearCancionConGenero, name='mod3'),


path('eliminar/<id>/',delete, name='eliminar'),



]
