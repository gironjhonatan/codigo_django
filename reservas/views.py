from django.shortcuts import render, redirect
from .models import Solicitud
from .models import Cliente
from .forms import ClienteForm,SolicitudForm, CustomUserCreationForm
from django.contrib import messages

from django.shortcuts import render
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html')

def usuario(request):
    clientes = Cliente.objects.all()
    return render(request, "usuario/lista_usuario.html", {'clientes': clientes})

def reserva(request):
    reservas = Solicitud.objects.all()
    return render(request, "salon/lista_reserva.html", {'reservas': reservas})

def crear_usuario(request):
    formulario1 = ClienteForm(request.POST or None, request.FILES or None)
    if formulario1.is_valid():
        formulario1.save()
        return redirect('usuario')
    return render(request, "usuario/crear_usuario.html",{"formulario1":formulario1})

def crear_reserva(request):
    formulario2 = SolicitudForm(request.POST or None, request.FILES or None)
    if formulario2.is_valid():
        formulario2.save()
        return redirect('reserva')
    return render(request, "salon/crear_reserva.html",{"formulario2":formulario2})

def editar_usuario(request, id_cliente):
    usuario = usuario.objects.get(id_cliente=id_cliente)
    formulario1 = ClienteForm(request.POST or None, request.FILES or None)
    print(formulario1) 
    return render(request, "usuario/editar_usuario.html",{'formulario1':formulario1})


def editar_reserva(request, id_solicitud):
    reserva = reserva.objects.get(id_solicitud=id_solicitud)
    formulario2 = ClienteForm(request.POST or None, request.FILES or None)
    return render(request, "salon/editar_reserva.html",{'formulario2':formulario2})

def reservas_solicitadas(request):
    return render(request, "solicitudes/reservas_solicitadas.html")

def eliminarr(request, id_solicitud):
    reserva = Solicitud.objects.get(id_solicitud=id_solicitud)
    reserva.delete()
    return redirect('reserva')

def eliminaru(request, id_cliente):
    usuario = Cliente.objects.get(id_cliente=id_cliente)
    usuario.delete()
    return redirect('usuario')

def registro(request):
    data= {
        'form': CustomUserCreationForm
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password= formulario.cleaned_data["password1"])
            login(request, user)
            #messages(request, "resgistro exitoso")
            return redirect(to="inicio")
        data["form"] = formulario
    return render(request, 'paginas/registro.html', data)
