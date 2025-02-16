from django import forms
from .models import Cursos

class CursosForm(forms.ModelForm):
    class Meta:
        model = Cursos
        fields = ['nombre', 'descripcion', 'fecha_inicio', 'fecha_fin', 'activo']
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'type': 'date'}),
        }
