from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from applications.home.views import FechaMixin

# Create your views here.
from .models import inicioSesion
from .forms import IngresoForm

class PruebaView(LoginRequiredMixin, FechaMixin, TemplateView):
    template_name = 'consultar-resultados/consultar.html'
    login_url=reverse_lazy('user_app:user-login')



class ConsultasCreateView(LoginRequiredMixin, FechaMixin, CreateView):
    template_name = 'consultar-resultados/consultar.html'
    model = inicioSesion
    form_class = IngresoForm
    success_url = 'resultados/'
    login_url=reverse_lazy('user_app:user-login')

    # def get_queryset(self):
    #     user = self.request.POST.get('nomuser')
    #     passw = self.request.POST.get('contraseña')
        
class resultView(FechaMixin, LoginRequiredMixin,TemplateView):
    template_name = 'consultar-resultados/resultados.html'
    login_url=reverse_lazy('user_app:user-login')