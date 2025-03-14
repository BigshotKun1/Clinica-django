# Generated by Django 5.1.6 on 2025-02-11 19:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('medicos', '0001_initial'),
        ('pacientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Atencion',
            fields=[
                ('id_atencion', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('valor_atencion', models.DecimalField(decimal_places=2, max_digits=10)),
                ('id_medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicos.medico')),
                ('id_paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pacientes.paciente')),
            ],
        ),
    ]
