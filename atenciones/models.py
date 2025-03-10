from django.db import models
from pacientes.models import Paciente
from medicos.models import Medico

class Atencion(models.Model):
    id_atencion = models.AutoField(primary_key=True)
    id_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    id_medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    fecha = models.DateField()
    motivo = models.CharField(max_length=255, null=True, blank=True)
    valor_atencion = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Atención de {self.id_paciente} con {self.id_medico}'
