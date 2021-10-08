
from django.contrib import admin
from .models import (Sede, 
    Consultorio, 
    Medico,
    Usuario,
    
    Consulta)


# Register your models here.

class ConsultaAdmin(admin.ModelAdmin):
    list_display = (
        'usuario',
        'codigo',
        'sede',
        'consultorio',
        'Historia',
        'fecha_solicitud'
    )

admin.site.register(Consulta, ConsultaAdmin)

class UsuarioAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'documento',
        'nombre',
        'apellido',
        'edad',
        'direccion',
        'telefono',
        'email'
    )

admin.site.register(Usuario, UsuarioAdmin)


class MedicoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'sede',
        'documento',
        'nombre',
        'apellido',
        'especialidad',
        'nombre_completo'
    )

    def nombre_completo(self, obj):
        return obj.nombre + ' ' + obj.apellido

admin.site.register(Medico, MedicoAdmin)



class ConsultorioAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'sede',
        'num_consultorio'
    )

admin.site.register(Consultorio, ConsultorioAdmin)


class SedeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombre_sede',
        'direccion_sede',
        'telefono_sede',
        'correo_sede'
    )

admin.site.register(Sede, SedeAdmin)


