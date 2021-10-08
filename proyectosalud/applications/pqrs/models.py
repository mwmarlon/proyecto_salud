from django.db import models

# Create your models here.

#Modelo de PQRS, formulario

class formularioPQRS (models.Model):

    #Lista de típos de documentos
    doc_Choices = (
        ('0','Cédula de ciudadanía'),
        ('1','Cédula de extranjería'),
        ('2','NIT'),
    )
    
    #Lista de opciones de ubicaciones posibles 
    locations = (
        ('0','Oficinas'),
        ('1','Centros de atención'),
        ('2','Telefónico'),
    )

    #Campos del formulario| Tabla
    type_document = models.CharField(
        'Típo de documento', 
        max_length=12,
        choices=doc_Choices,
    )

    identificacion = models.CharField(
        'Número documento', 
        max_length=12,
        #help_text="Escriba el número de su documento"
    )

    first_name = models.CharField(
        'Nombres', 
        max_length=50,
        #help_text="Escriba sus nombres"
    )

    last_name = models.CharField(
        'Apellidos', 
        max_length=50,
        #help_text="Escriba sus apellidos"
    )

    #   Campos de detalle del PQRS
    locate_hppnd = models.CharField(
        'ubicación del hecho',
        max_length=50, 
        choices=locations
    )

    city_name = models.CharField(
        'Ciudad',
        max_length=20
    )

    dscrp_happ = models.CharField(
        'Descripción de hechos',
        max_length=250
    )

    def __str__(self) -> str:
        return str(self.id) + ' | ' + self.identificacion + ' | ' + self.first_name + ' | ' + self.last_name
