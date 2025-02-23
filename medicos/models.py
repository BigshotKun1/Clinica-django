from django.db import models
from usuarios.views import Usuario


class Medico(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)  #Relación 1:1
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    rut = models.CharField(max_length=12, unique=True)
    especialidad = models.CharField(max_length=100, blank=True, null=True)  
    telefono = models.CharField(max_length=15, blank=True, null=True)
    sueldo = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    fecha_contratacion = models.DateField(blank=True, null=True)
    

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.especialidad}"
    

