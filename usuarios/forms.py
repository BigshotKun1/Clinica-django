from django import forms
from .models import Usuario

class RegistroUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre_usuario', 'email', 'clave', 'rol']
    
    clave = forms.CharField(widget=forms.PasswordInput)

class IniciarSesionUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['email', 'clave']
    
    clave = forms.CharField(widget=forms.PasswordInput)
