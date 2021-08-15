from django.forms import widgets
from django import forms
from DjangoTicketApp.models import *

class  EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = [
            'nombre',
            'nit',
            'telefono',
            'direccion',
            'correo',
        ]
        labels = {
            'nombre' : 'Nombre',
            'nit' : 'Nit',
            'telefono' : 'Telefono',
            'direccion' : 'Direccion',
            'correo' : 'Correo',
        }
        widgets = {
            'nombre' : forms.TextInput(attrs={'class':'form-control'}),
            'nit'  : forms.TextInput(attrs={'class':'form-control'}),
            'telefono'  : forms.TextInput(attrs={'class':'form-control'}),
            'direccion'  : forms.TextInput(attrs={'class':'form-control'}),
            'correo'  : forms.EmailInput(attrs={'class':'form-control'}),
        }


class  ProyectoForm(forms.ModelForm):
    class Meta:
        model = ProyectoDesarrollo
        fields = [
            'empresaAsociada',
            'descripcion',
        ]
        labels = {
            'empresaAsociada' : 'empresa Asociada',
            'descripcion' : 'descripcion de el proyecto',

        }
        widgets = {
            'empresaAsociada' : forms.Select(attrs={'class':'form-control'}),
            'descripcion'  : forms.TextInput(attrs={'class':'form-control'}),
        }

class  HistoriaForm(forms.ModelForm):
    class Meta:
        model = HistoriaUsuario
        fields = [
            'idProyectoDesarrollo',
            'descripcion',
        ]
        labels = {
            'idProyectoDesarrollo' : 'proyecto al que esta asociado Asociado',
            'descripcion' : 'descripcion de la historia',

        }
        widgets = {
            'idProyectoDesarrollo' : forms.Select(attrs={'class':'form-control'}),
            'descripcion'  : forms.TextInput(attrs={'class':'form-control'}),
        }

class  TicketForm(forms.ModelForm):
    class Meta:
        model = TicketDesarrollo
        fields = [
            'idHistoriaUsuario' ,
            'usuario',
            'descripcion', 
            'estatus',
        ]
        labels = {
            'idHistoriaUsuario' : 'Historia Usuario Asociada',
            'usuario' : 'usuario responsable',
            'descripcion': 'descripcion del ticket',
            'estatus': 'estado del ticket',

        }
        widgets = {
            'idHistoriaUsuario' : forms.Select(attrs={'class':'form-control'}),
            'usuario'  : forms.TextInput(attrs={'class':'form-control'}),
            'descripcion'  : forms.TextInput(attrs={'class':'form-control'}),
            'estatus': forms.Select(attrs={'class':'form-control'}),
        }