from django.contrib import admin
from .models import Autor, Canciones , AutorCancion, Lista
# Register your models here.

admin.site.register(Autor)
admin.site.register(Canciones)
admin.site.register(AutorCancion)
admin.site.register(Lista)
