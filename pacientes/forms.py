from django import forms
from .models import Paciente 
from usuarios.models import Usuario


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
        fields = ['usuario', 'nombre', 'apellido', 'sexo', 'telefono', 'direccion', 'antecedentes'] 
    
    usuario = forms.ModelChoiceField(queryset=Usuario.objects.filter(rol='paciente'), required=True)

    

