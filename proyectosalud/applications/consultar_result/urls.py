
from django.contrib import admin
from django.urls import path


from . import views
app_name = "consultar_app"

urlpatterns = [
    path(
        'consultar-resultados/', 
        views.PruebaView.as_view(), 
        name='consulta1'
    ),
    path(
        'consultar-form/', 
        views.ConsultasCreateView.as_view(),
        name='consulta2'
    ),
    path('resultados/', views.resultView.as_view()),
]
