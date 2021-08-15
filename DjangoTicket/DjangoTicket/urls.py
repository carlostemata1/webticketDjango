"""DjangoTicket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from DjangoTicketApp.views import *
from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', base),
    path('base/', base),
    path('listarEmpresa/', ListarEmpresa.as_view()),
    path('listarProyecto/', ListarProyecto.as_view()),
    path('listarHistoria/', ListarHistoria.as_view()),
    path('listarTicket/', ListarTicket.as_view()),
    path('crearEmpresa/', CrearEmpresa.as_view()),
    path('crearProyecto/', CrearProyecto.as_view()),
    path('crearHistoria/', CrearHistoria.as_view()),
    path('crearTicket/', CrearTicket.as_view()),
    path('actualizarTicket/<pk>', ActualizarTicket.as_view()),

]
