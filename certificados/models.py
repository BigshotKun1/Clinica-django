from django.db import models


# Create your models here.
class Certificado(models.Model):
    id_certificado = models.AutoField(primary_key=True)
    id_atencion = models.ForeignKey('atenciones.Atencion', on_delete=models.CASCADE)
    fecha_emision = models.DateField()
    descripcion = models.TextField()

    def __str__(self):
        return f'{self.fecha_emision}'
    