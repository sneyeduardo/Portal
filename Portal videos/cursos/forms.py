from django import forms
from .models import Clase

class ClaseForm(forms.ModelForm):
    class Meta:
        model = Clase
        # Los campos que el administrador podrá llenar
        fields = ['curso', 'titulo', 'descripcion', 'vimeo_id', 'orden', 'duracion', 'fecha_estreno']
        
        # Le ponemos un calendario bonito al campo de fecha
        widgets = {
            'fecha_estreno': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
        }