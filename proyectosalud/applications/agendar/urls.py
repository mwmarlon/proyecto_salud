from django.contrib import admin
from django.urls import path, re_path, include
from .import views

app_name = 'agendar_app'

urlpatterns = [
    path(
        'sedes/', 
        views.Sedes_a.as_view(),
        name='cita'
    ),
    path(
        'agendar/', 
        views.ConsultaCreateView.as_view(),
        name='agenda'
    ),
    path(
        'recordatorio_cita/', 
        views.RecordatorioView.as_view(),
        name='recordatorio'
    )    
]
