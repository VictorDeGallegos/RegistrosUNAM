from django import forms
from .models import position
from .models import employee


class employeeForm(forms.ModelForm):

    class Meta:
        model = employee
        fields = ("NombreCompleto", "CURP",
                  "numero_de_empleado", "sueldo", "position")
        widgets = {
            'NombreCompleto': forms.TextInput(attrs={'class': 'form-control', 'id': 'NombreCompleto', 'placeholder': 'Nombre Completo'}),
            'CURP': forms.TextInput(attrs={'class': 'form-control', 'id': 'CURP', 'placeholder': 'CURP'}),
            'numero_de_empleado': forms.TextInput(attrs={'class': 'form-control', 'id': 'mobNo', 'placeholder': '# de trabajador'}),
            'sueldo': forms.TextInput(attrs={'class': 'form-control', 'id': 'sueldo', 'placeholder': '3000 ejemplo'}),
            'position': forms.Select(attrs={'class': 'form-control', 'id': 'exampleFormControlSelect1'}),
        }
