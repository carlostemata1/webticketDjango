from django.views.generic.edit import UpdateView
from DjangoTicketApp.models import *
from django.http import HttpResponse
from django.shortcuts import redirect, render
from DjangoTicketApp.forms import *
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView


def base(request):
    return render(request,'base/base.html')

class ListarEmpresa(ListView):
    model = Empresa
    template_name = 'toDo/listarEmpresa.html'

class ListarProyecto(ListView):
    model = ProyectoDesarrollo
    template_name = 'toDo/listarProyecto.html'


class ListarHistoria(ListView):
    model = HistoriaUsuario
    template_name = 'toDo/listarHistoria.html'


class ListarTicket(ListView):
    model = TicketDesarrollo
    template_name = 'toDo/listarTicket.html'


#-----crear --------

class CrearEmpresa(CreateView):
    model = Empresa
    form_class = EmpresaForm
    template_name = 'toDo/formEmpresa.html'
    success_url = reverse_lazy('../listarEmpresa/')


class CrearProyecto(CreateView):
    model = ProyectoDesarrollo
    form_class = ProyectoForm
    template_name = 'toDo/formProyecto.html'
    success_url = reverse_lazy('DjangoTicketApp:listarProyecto/')


class CrearHistoria(CreateView):
    model = HistoriaUsuario
    form_class = HistoriaForm
    template_name = 'toDo/formHistoria.html'
    success_url = reverse_lazy(':/listarHistoria/')


class CrearTicket(CreateView):
    model = TicketDesarrollo
    form_class = TicketForm
    template_name = 'toDo/formTicket.html'
    success_url = reverse_lazy('listarTicket')
    

#-------actualizar ticket ------

class ActualizarTicket(UpdateView):
    model = TicketDesarrollo
    form_class = 'toDo/ActualizarTicket'
    template_name = 'toDo/formTicket.html'
    success_url = reverse_lazy('../listarTicket/')