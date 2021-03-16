from crum import get_current_user
from django.db import models
from django.contrib.auth.models import User


from .mod import audi
# Create your models here.

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.PositiveBigIntegerField()
    def __str__(self):
         return self.nombre


class Canciones(models.Model):
    titulo = models.CharField(max_length=100)
    fechalanzamiento = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    url= models.URLField(unique=True , null=True, blank=True)
    imagen = models.ImageField(upload_to='Caratulas', null=True, blank=True)


    def __str__(self):
        return self.titulo


class AutorCancion(models.Model):
    genero = [
        ('ROCK', 'ROCK'),
        ('POP', 'POP'),
        ('ALTERNATIVA', 'ALTERNATIVA'),
    ]
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, default='Undefinided')
    cancion = models.ForeignKey(Canciones, on_delete=models.CASCADE)
    genero = models.CharField(max_length=12, choices=genero, null=True, blank=True)
    def __str__(self):
        return '{} de {}'.format(self.cancion.titulo, self.autor.nombre)




class Lista(audi):
    cancionL= models.ForeignKey(AutorCancion, on_delete=models.CASCADE)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):

        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.usuariocreatedor = user
            else:
                self.usuariocreatedor = user

        super(Lista, self).save()

