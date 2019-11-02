from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.views.generic.detail import DetailView

from django.urls import reverse_lazy

from .models import *

from django.http import HttpResponseRedirect

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin


def cargar_inicio(request):
    return render(request, "apps/index.html")

class TablaList(ListView):
    model = tabla
    template_name = 'apps/informes.html'

class RegistrarTablaCreate(CreateView):
    model = tabla
    fields = ['Actividades','MantenimientoP','MantenimientoC','Fecha','FechaViso']
    template_name = 'apps/RegistrarActividades.html'
    success_url = reverse_lazy('Registrar_Actividades')