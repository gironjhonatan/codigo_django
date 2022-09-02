from dataclasses import field
from django import forms
from .models import Solicitud, Cliente, UsuariosRegistro
from django.contrib.auth.forms import UserCreationForm

class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = '__all__'
        exclude = []

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        exclude = []

class UsuariosRegistroForm(forms.ModelForm):

    class Meta:
        model = UsuariosRegistro
        field =  '__all__'
        exclude = []

class CustomUserCreationForm(UserCreationForm):
    pass