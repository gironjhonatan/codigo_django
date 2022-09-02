from django.db import models

class Cliente (models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    tel = models.CharField(max_length=13)
    correo = models.CharField(max_length=30)
    departamento = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=30)
    edad = models.CharField(max_length=10)

    def __str__(self):
        fila1 = "Nombre:" + self.nombre + " - " + "Tel:" + self.tel + " - " 
        + "correo: " + self.correo + " - " + "Departamento:" + self.departamento 
        + " - " + "Ciudad:" + self.ciudad + " - " + "Edad:" + self.edad
        return fila1
class Solicitud (models.Model):
    id_solicitud = models.AutoField(primary_key=True)
    fecha = models.DateField()
    no_personas = models.CharField(max_length=10)
    motivo = models.CharField(max_length=40)
    observaciones = models.CharField(max_length=200)
    estado = models.CharField(max_length=15)

    def __str__(self):
        fila2 = "Fecha:" + self.fecha + " - " + "No.personas:" + self.no_personas + " - " 
        + "Motivo: " + self.motivo + " - " + "observaciones:" + self.observaciones 
        + " - " + "Estado:" + self.estado
        return fila2
class UsuariosRegistro (models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    correo = models.CharField(max_length=40)
    password1 = models.CharField(max_length=20)
    password2 = models.CharField(max_length=20)

    def __str__(self):
        fila3 = "Nombre:" + self.nombre + " - " + "Correo:" + self.correo + " - "
        + "Pass1:" + self.password1 + " - " + "Pass2:" + self.password2
        return fila3
