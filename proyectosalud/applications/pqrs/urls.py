from django.contrib import admin
from django.urls import (
    path
    # re_path
)

#Se importan las vistas del mismo nivel del URLs
from . import views

app_name = "pqrs_app"

urlpatterns = [
    path(
        'pqrs-form/', 
        views.formularioPQRSCreateView.as_view(),
        name="formPQRS",
    ),
    path(
        'success-form/',
        views.SuccessForm.as_view(),
        name='successForm'
    ),
]
