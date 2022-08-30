from django import forms
from .models import Solicitud, Cliente
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

class CustomUserCreationForm(UserCreationForm):
    pass