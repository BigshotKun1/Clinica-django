from django import forms
from .models import Medico 

class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = '__all__'

    fecha_contratacion = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'placeholder': 'YYYY-MM-DD'}), 
    )
 