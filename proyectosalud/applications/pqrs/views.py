from django.forms import forms
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

#Se importan vistas genéricas de django
from django.views.generic import (
    TemplateView,
    #ListView,
    CreateView
)
from django.urls import reverse_lazy
from django import forms
from applications.home.views import FechaMixin

# Create your views here.

"""
    Se importa el models para el formulario
        - se usa una vista genérica de creación
        - Se crea un Success para el formulario
"""
from .models import formularioPQRS

class formularioPQRSCreateView(LoginRequiredMixin, FechaMixin, CreateView):
    template_name = "pqrs/pqrsForm.html"
    model = formularioPQRS
    context_object_name = "formPQRS"
    fields=('__all__')
    success_url = reverse_lazy("pqrs_app:successForm")
    login_url=reverse_lazy('user_app:user-login')

    def form_valid(self, form: formularioPQRS):
        return super().form_valid(form)

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()

        form = super(formularioPQRSCreateView, self).get_form(form_class)
        form.fields['identificacion'].widget = forms.TextInput(attrs={'placeholder': 'Su número de cédula'})
        return form

class SuccessForm(LoginRequiredMixin, TemplateView):
    template_name = "pqrs/successForm.html"
    login_url=reverse_lazy('user_app:user-login')

