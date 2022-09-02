from django.shortcuts import render, redirect
from .models import Solicitud
from .models import Cliente
from .models import UsuariosRegistro
from .forms import ClienteForm,SolicitudForm, UsuariosRegistroForm

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
    return render(request, 'paginas/login_usuarios.html')

def registro(request):
    formulario3 = UsuariosRegistroForm(request.POST or None, request.FILES or None)
    if formulario3.is_valid():
       formulario3.save()
       return redirect(request, 'registro')
    return render(request, "login/registro.html",{"formulario3":formulario3})

    


    # data= {
    #     'form': CustomUserCreationForm
    # }

    # if request.method == 'POST':
    #     formulario = CustomUserCreationForm(data=request.POST)
    #     if formulario.is_valid():
    #         formulario.save()
    #         user = authenticate(username=formulario.cleaned_data["username"], password= formulario.cleaned_data["password1"])
    #         login(request, user)
    #         #messages(request, "resgistro exitoso")
    #         return redirect(to="inicio")
    #     data["form"] = formulario
   
