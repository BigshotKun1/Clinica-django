from django import forms
from .models import Atencion
from pacientes.models import Paciente
from medicos.models import Medico

class AtencionForm(forms.ModelForm):
    class Meta:
        model = Atencion
        fields = 'id_paciente', 'id_medico', 'fecha', 'motivo', 'valor_atencion'
    
    fecha = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'placeholder': 'YYYY-MM-DD'}),  # Placeholder indicando el formato
    )

     # Personalización de los labels y widgets
    id_paciente = forms.ModelChoiceField(
        queryset=Paciente.objects.all(),
        label="Selecciona al Paciente",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    id_medico = forms.ModelChoiceField(
        queryset=Medico.objects.all(),
        label="Selecciona al Médico",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    valor_atencion = forms.DecimalField(
        label="Valor de la Atención",
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el valor'})
    )