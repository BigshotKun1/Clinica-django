from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password

class UsuarioManager(BaseUserManager):
    def create_user(self, email, nombre_usuario, rol, password=None):
        if not email:
            raise ValueError("El usuario debe tener un email")
        usuario = self.model(
            email=self.normalize_email(email), 
            nombre_usuario=nombre_usuario, 
            rol=rol
        )
        usuario.set_password(password) 
        usuario.save(using=self._db)
        return usuario

    def create_superuser(self, email, nombre_usuario, rol, password):
        usuario = self.create_user(email, nombre_usuario, rol, password)
        usuario.is_admin = True
        usuario.is_staff = True  
        usuario.is_superuser = True  
        usuario.save(using=self._db)
        return usuario    

class Usuario(AbstractBaseUser):
    id_usuarios = models.AutoField(primary_key=True)
    nombre_usuario = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    rol = models.CharField(
        max_length=20,
        choices=[
            ('admin', 'Administrador'),
            ('medico', 'Médico'),
            ('paciente', 'Paciente'),
        ],
    )

    password = models.CharField(max_length=255) 

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre_usuario', 'rol']

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
