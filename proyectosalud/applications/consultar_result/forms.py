from django import forms

from .models import inicioSesion

class IngresoForm(forms.ModelForm):
    """Form definition for Ingreso."""

    class Meta:
        """Meta definition for Ingresoform."""
        model = inicioSesion
        fields = (
            'nomuser',
            'contraseña'
            )
        widgets = {
            'nomuser': forms.TextInput(
                attrs= {
                    'placeholder': 'Nombre de Usuario'
                } 
            ),
            'contraseña': forms.TextInput(
                attrs= {
                    'placeholder': 'Contraseña'
                } 
            )
        }

    
