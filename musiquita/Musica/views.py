from django.shortcuts import render, redirect, get_object_or_404
from .models import AutorCancion, Autor, Canciones, Lista
from .forms import AutorCancionF, AutorF, CancionF, ListaF , restrationF
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate ,  login
# Create your views here.

def inicio(request):
    template = 'Musica/inicio.html'

    return render(request, template)


@permission_required('Musica.add.canciones')
def Administracion(request):
    template = 'Musica/Administracion.html'
    data = {
        'cancionesT': AutorCancion.objects.all(),
        'Autor': Autor.objects.all(),
        'canciones': Canciones.objects.all(),

    }
    return render(request, template, data)

@login_required()
def home(request):
    template = 'Musica/raiz.html'
    informacion = AutorCancion.objects.all()
    informacionpop = AutorCancion.objects.filter(genero='POP')
    informacionrock = AutorCancion.objects.filter(genero='ROCK')
    informacionalternativo = AutorCancion.objects.filter(genero='ALTERNATIVA')
    data ={
        'data': CancionF(),
        'infopop':informacionpop,
        'inforock':informacionrock,
        'infoalternativo':informacionalternativo,
        'info':informacion,
    }
    if request.method == 'POST':
        formulario = CancionF(data=request.POST , files=request.FILES)
        try:
            if formulario.is_valid():
                formulario.save()
                return redirect(to='home')
        except Exception as e:
            print(e , 'ESTE ES EL ERROR')

    return render(request,template, data)

@login_required()
def listaRep(request):
    template = 'Musica/listarep.html'
    userr = request.user
    print(userr)
    datas = Lista.objects.filter(usuariocreatedor=userr)
    data={
        'form': ListaF(),
        'data': datas
    }
    if request.method == 'POST':
        formulario = ListaF(data=request.POST)
        try:
            if formulario.is_valid():
                formulario.save()
                return redirect(to='listarep')
        except Exception as e:
            print(e , 'ESTE ES EL ERROR')

    return render(request, template, data)


@permission_required('Musica.add.canciones')
def Crearcancion(request):
    template = 'Musica/modals/CrearCancion.html'
    data = {
        'cancion': CancionF(),

    }
    if request.method == 'POST':
        formulario = CancionF(data=request.POST,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to='administracion')



        data["mensaje"] = "modificado corectamente"
    else:

        data["error"] = "no se ah modificado nada"


    return render(request, template, data)
@permission_required('Musica.add.canciones')
def CrearAutor(request):
    template = 'Musica/modals/CrearAutor.html'
    data = {
        'AUTOR': AutorF(),
    }
    if request.method == 'POST':
        formulario = AutorF(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(to='administracion')

        data["mensaje"] = "modificado corectamente"
    else:

        data["error"] = "no se ah modificado nada"


    return render(request, template, data)
@permission_required('Musica.add.canciones')
def CrearCancionConGenero(request):
    template = 'Musica/modals/CrearCancionConGenero.html'
    data = {
        'AutorCancion': AutorCancionF(),
    }
    if request.method == 'POST':
        formulario = AutorCancionF(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(to='administracion')

        data["mensaje"] = "modificado corectamente"
    else:

        data["error"] = "no se ah modificado nada"


    return render(request, template, data)


def registro(request):
    template = 'registration/registro.html'
    data = {
        'form': restrationF()
    }
    if request.method == 'POST':
        formulario =  restrationF(data=request.POST)
        try:
            if formulario.is_valid():
                fg = formulario.cleaned_data
                usuario = fg.get('username')
                password1 = fg.get('password1')
                print(usuario)
                formulario.save()
                user = authenticate(username=usuario, password=password1)
                login(request, user)
                return redirect(to='homes')
        except Exception as e:
            print(e)
    else:
        print('no entre')

    return render(request, template, data)


@login_required()
def pop(request):
    template = 'Musica/pop.html'
    informacion = Lista.objects.filter(cancionL__genero='POP')
    data ={
        'info':informacion
    }
    return render(request,template, data)


@login_required()
def rock(request):
    template = 'Musica/rock.html'
    informacion = Lista.objects.filter(cancionL__genero='ROCK')
    data ={
        'info':informacion
    }
    return render(request,template, data)


@login_required()
def alternativo(request):
    template = 'Musica/alternativa.html'
    informacion = Lista.objects.filter(cancionL__genero='ALTERNATIVA')
    data ={
        'info':informacion
    }
    return render(request,template, data)


def delete(request, id):
    falla = get_object_or_404(Lista, id=id)
    falla.delete()
    print('SE ELIMINO')
    return redirect(to='listarep')