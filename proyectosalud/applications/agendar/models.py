from django.db import models
from datetime import date

# Create your models here.

class Sede(models.Model):
    nombre_sede = models.CharField(
        max_length=20, 
        help_text='nombre sede'
    )
    direccion_sede = models.CharField(
        max_length=50
    )
    telefono_sede = models.CharField(
        max_length=50
    )
    correo_sede = models.CharField(
        max_length=50
    )

    class Meta:

        verbose_name = 'Sede'
        verbose_name_plural = 'Sedes'
        ordering = ['nombre_sede']

    def __str__(self):
        return self.nombre_sede


class Consultorio(models.Model):
    sede = models.ForeignKey(
        Sede, 
        on_delete=models.CASCADE
    )
    num_consultorio = models.CharField(
        max_length=3
    )

    class Meta:
        ordering = ['sede']

    def __str__(self):
        return self.num_consultorio

class Medico(models.Model):
    sede = models.ForeignKey(
        Sede, 
        on_delete=models.CASCADE
    )
    #num_consultorio = models.ForeignKey(
    #    Consultorio, 
    #    on_delete=models.CASCADE
    #)
    documento = models.CharField(
        max_length=50, 
        unique=True
    )
    nombre = models.CharField(
        max_length=30
    )
    apellido = models.CharField(
        max_length=30
    )
    especialidad = models.CharField(
        max_length=30
    )
    
    class Meta:
        ordering = ['nombre', 'apellido']

    def __str__(self):
        return self.nombre


class Usuario(models.Model):
    documento = models.CharField(
        max_length=15
    )
    nombre = models.CharField(
        max_length=30
    )
    apellido = models.CharField(
        max_length=30
    )
    direccion = models.CharField(
        max_length=40
    )
    edad = models.PositiveIntegerField(default=0)
    telefono = models.CharField(
        max_length=15
    )
    email = models.EmailField(
        max_length=50
        )

    class Meta:
    
        verbose_name = 'usuario'
        verbose_name_plural = 'usuarios'

    def __str__(self):
        return self.nombre

class Consulta(models.Model):
    usuario = models.ForeignKey(
        Usuario, 
        on_delete=models.CASCADE
    )
    codigo = models.CharField(
        max_length=10
    )
    sede = models.ForeignKey(
        Sede, on_delete=models.CASCADE
    )
    consultorio = models.ForeignKey(
        Consultorio, 
        on_delete=models.CASCADE
    )
    #hora = models.CharField(
    #    max_length=10
    #)
    Historia = models.ImageField(
        upload_to='history', 
        blank=True, null=True
    )
    fecha_solicitud=date.today()
    
    class Meta:
        verbose_name = 'consulta'
        verbose_name_plural = 'consultas'

    def __str__(self):
        return self.codigo