from django import forms
from .models import Autor, AutorCancion, Canciones, Lista
from django.contrib.auth.forms import UserCreationForm

class AutorF(forms.ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'


class AutorCancionF(forms.ModelForm):
    class Meta:
        model = AutorCancion
        fields = '__all__'


class CancionF(forms.ModelForm):
    class Meta:
        model = Canciones
        fields = '__all__'
        exclude = {'fechalanzamiento'}

class ListaF(forms.ModelForm):
    class Meta:
        model = Lista
        fields = '__all__'
        exclude = {'usuariocreatedor'}

class restrationF(UserCreationForm):
    pass

