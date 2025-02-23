from django import forms
from .models import Atencion

class AtencionForm(forms.ModelForm):
    class Meta:
        model = Atencion
        fields = 'id_paciente', 'id_medico', 'fecha', 'valor_atencion'
    
    fecha = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'placeholder': 'YYYY-MM-DD'}),  # Placeholder indicando el formato
    )