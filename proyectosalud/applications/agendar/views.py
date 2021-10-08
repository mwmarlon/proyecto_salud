from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (ListView, CreateView,TemplateView)
from django.contrib.auth.mixins import LoginRequiredMixin

from applications.home.views import FechaMixin


#modelo local

from .models import Sede, Consulta, Usuario
from .forms import ConsultaForm

class RecordatorioView(LoginRequiredMixin, FechaMixin,TemplateView):
    template_name = "agendar/recordatorio.html"
    login_url=reverse_lazy('user_app:user-login')

class ConsultaCreateView(LoginRequiredMixin, FechaMixin, CreateView):
    model = Consulta 
    template_name = "agendar/add.html/"
    form_class = ConsultaForm
    success_url = reverse_lazy('agendar_app:recordatorio')
    login_url=reverse_lazy('user_app:user-login')


class Sedes_a(LoginRequiredMixin, FechaMixin, ListView):
    #model = Sede
    context_object_name = 'datos_sedes'
    template_name = "agendar/sedes.html"
    login_url=reverse_lazy('user_app:user-login')

    def get_queryset(self):

        return Sede.objects.all()
