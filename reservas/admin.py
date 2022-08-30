from django.contrib import admin

from .models import Cliente
from .models import Solicitud

admin.site.register(Cliente)
admin.site.register(Solicitud)
