from django import forms
from .models import Solicitud, Cliente
from django.contrib.auth.forms import UserCreationForm

class SolicitudForm(forms.Form):
    class Meta:
        model = Solicitud
        field = '__all__'

class ClienteForm(forms.Form):
    class Meta:
        model = Cliente
        field = '__all__'

class CustomUserCreationForm(UserCreationForm):
    pass