from django import forms
from .models import *

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto

        fields = [
            'nombre',
            'precio',
            'cantidad'
        ]

        labels = {
            'nombre' : 'Nombre',
            'precio' : 'Precio',
            'cantidad' : 'Cantidad'
        }

