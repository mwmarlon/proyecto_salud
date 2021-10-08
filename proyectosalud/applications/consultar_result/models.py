from django.db import models




# Create your models here.
class inicioSesion(models.Model):
    nomuser = models.CharField('nomuser', max_length=50)
    contraseña = models.CharField('contraseña', max_length=50)

    class Meta:
        verbose_name_plural = 'Inicio Sesion'

    def __str__(self) -> str:
        return str(self.id) + self.nomuser + ' ' + self.contraseña