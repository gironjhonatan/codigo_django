from django.contrib import admin

from .models import Cliente
from .models import Solicitud
from .models import UsuariosRegistro

admin.site.register(Cliente)
admin.site.register(Solicitud)
admin.site.register(UsuariosRegistro)
