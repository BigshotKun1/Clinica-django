from django import forms
from .models import Paciente 

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'

    fecha_registro = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'placeholder': 'YYYY-MM-DD'}),  # Placeholder indicando el formato
    )

    fecha_nacimiento = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'placeholder': 'YYYY-MM-DD'}),  # Placeholder indicando el formato
    )

class PacienteFormEdit(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nombre', 'apellido', 'sexo', 'telefono', 'email', 'direccion', 'antecedentes'] 
    