from django.db import models
from usuarios.models import Usuario  # Asegúrate de importar el modelo Usuario

class Paciente(models.Model):
    id_paciente = models.AutoField(primary_key=True)
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, limit_choices_to={'rol': 'paciente'}, null= True, blank = True)  # Solo pacientes
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    rut = models.CharField(max_length=12, unique=True)
    fecha_nacimiento = models.DateField()
    sexo = models.CharField(max_length=1, choices=[('M', 'Masculino'), ('F', 'Femenino')])
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=255)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    antecedentes = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
