from django import forms
from .models import Medico
from usuarios.models import Usuario  # Importar el modelo de Usuario

class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = '__all__'  # Esto incluirá todos los campos del modelo Medico

    # Personalizar el campo 'usuario' para mostrar solo los usuarios con rol 'medico'
    usuario = forms.ModelChoiceField(queryset=Usuario.objects.filter(rol='medico'), empty_label="Selecciona un usuario", required=True)

    # Personalización para el campo 'fecha_contratacion'
    fecha_contratacion = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'placeholder': 'YYYY-MM-DD'}), 
    )
