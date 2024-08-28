# tecnologia/forms.py

from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['codigo', 'descripcion', 'precio', 'tipo']
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
        }
    
    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio < 100:
            raise forms.ValidationError('El precio no puede ser menor a 100.')
        return precio