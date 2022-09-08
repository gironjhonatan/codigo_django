from pyexpat.errors import messages
from django.shortcuts import render, redirect
from .models import Solicitud
from .models import Cliente
from .forms import ClienteForm,SolicitudForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate


from django.shortcuts import render
from .models import *

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
    cliente  = Cliente.objects.get(id_cliente = id_cliente)
    formulario1 = ClienteForm(request.POST or None, request.FILES or None, instance = cliente)
    if formulario1.is_valid() and request.method == 'POST':
        formulario1.save()
        return redirect('usuario')
    return render(request, "usuario/editar_usuario.html",{'formulario1':formulario1})

def editar_reserva(request, id_solicitud):
    reserva = Solicitud.objects.get(id_solicitud = id_solicitud)
    formulario2 = SolicitudForm(request.POST or None, request.FILES or None, instance = reserva)
    if formulario2.is_valid() and request.method == 'POST':
        formulario2.save()
        return redirect('reserva')
    return render(request, "salon/editar_reserva.html",{'formulario2':formulario2})

def reservas_solicitadas(request):
    clientes = Cliente.objects.all()
    reservas = Solicitud.objects.all()
    return render(request, "solicitudes/reservas_solicitadas.html", {'clientes': clientes, 'reservas': reservas})

def eliminarr(request, id_solicitud):
    reserva = Solicitud.objects.get(id_solicitud=id_solicitud)
    reserva.delete()
    return redirect('reserva')

def eliminaru(request, id_cliente):
    usuario = Cliente.objects.get(id_cliente=id_cliente)
    usuario.delete()
    return redirect('usuario')

def login(request):
    if request.method == "POST":
        formulario = AuthenticationForm(request, data = request.POST)
        if formulario.is_valid():
            nom = formulario.cleaned_data.get("username")
            pas = formulario.cleaned_data.get("password")
            usu = authenticate(username = nom, password = pas)
            if usu is not None:
                return redirect("inicio")
            else:
                 messages.error(request, "no valido") 
    formulario = AuthenticationForm()
    return render(request, "paginas/login_usuarios.html",{"formulario":formulario})

def registro(request):
    if request.method == 'POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('inicio')
    else:
        formulario = UserCreationForm()
    return render(request, 'login/registro.html', {'formulario': formulario}) 

    
   
        

    




