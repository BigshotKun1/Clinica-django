# Generated by Django 5.1.6 on 2025-02-07 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuarios', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('clave', models.CharField(max_length=255)),
                ('rol', models.CharField(choices=[('admin', 'Administrador'), ('medico', 'Médico'), ('recepcionista', 'Recepcionista')], max_length=20)),
            ],
        ),
    ]
