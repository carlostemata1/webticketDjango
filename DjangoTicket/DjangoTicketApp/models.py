from django.db import models
from django.db.models.base import Model
from django.db.models.expressions import F
from django.db.models.fields import CharField


class Empresa(models.Model):
    nombre = models.CharField(max_length=50,blank=False, null=False)
    nit  = models.CharField(max_length=50,blank=False, null=False)
    telefono  = models.CharField(max_length=50,blank=False, null=False)
    direccion = models.CharField(max_length=50,blank=False, null=False)
    correo = models.EmailField()
    def __str__(self):
        return self.nombre


class ProyectoDesarrollo(models.Model):
    empresaAsociada = models.ForeignKey(Empresa, null=False, blank=False, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=50,blank=False, null=False)
    def __str__(self):
        return self.descripcion


class HistoriaUsuario(models.Model):
    idProyectoDesarrollo = models.ForeignKey(ProyectoDesarrollo, help_text="Proyecto al que pertenece", null=False, blank=False, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=50,blank=False, null=False)
    def __str__(self):
        return self.descripcion

class Estado(models.Model):
    estadodelTicket = models.CharField(max_length=50,blank=False, null=False)
    def __str__(self):
        return self.estadodelTicket

class  TicketDesarrollo(models.Model):
    idHistoriaUsuario = models.ForeignKey(HistoriaUsuario, help_text="la historia de usuario es", null=False, blank=False, on_delete=models.CASCADE)
    usuario = models.CharField(max_length=50,blank=False, null=False)
    descripcion = models.CharField (max_length=50,blank=False, null=False)
    estatus = models.OneToOneField(Estado, blank=False, null=False, on_delete=models.CASCADE)
    def __str__(self):
        return self.descripcion





    

