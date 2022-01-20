from django import forms
from .models import position
from .models import employee


class employeeForm(forms.ModelForm):

    class Meta:
        model = employee
        fields = ("nombre_completo", "CURP", "direccion",
                  "numero_de_empleado", "antiguedad", "sueldo", "position")
        widgets = {
            'nombre_completo': forms.TextInput(attrs={'class': 'form-control', 'id': 'nombre_completo', 'placeholder': 'Nombre Completo'}),
            'CURP': forms.TextInput(attrs={'class': 'form-control', 'id': 'CURP', 'placeholder': 'CURP'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'id': 'direccion', 'placeholder': 'Direccion'}),
            'numero_de_empleado': forms.TextInput(attrs={'class': 'form-control', 'id': 'mobNo', 'placeholder': 'No. de empleado'}),
            'antiguedad': forms.TextInput(attrs={'class': 'form-control', 'id': 'antiguedad', 'placeholder': 'Antiguedad'}),
            'sueldo': forms.TextInput(attrs={'class': 'form-control', 'id': 'sueldo', 'placeholder': '3000 ejemplo'}),
            'position': forms.Select(attrs={'class': 'form-control', 'id': 'exampleFormControlSelect1'}),
        }
