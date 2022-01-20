from django import forms
from .models import position
from .models import employee


class employeeForm(forms.ModelForm):

    class Meta:
        model = employee
        fields = ("nombre_completo", "CURP",
                  "numero_de_empleado", "sueldo", "position")
        widgets = {
            'nombre_completo': forms.TextInput(attrs={'class': 'form-control', 'id': 'nombre_completo', 'placeholder': 'Nombre Completo'}),
            'CURP': forms.TextInput(attrs={'class': 'form-control', 'id': 'CURP', 'placeholder': 'CURP'}),
            'numero_de_empleado': forms.TextInput(attrs={'class': 'form-control', 'id': 'mobNo', 'placeholder': '# de trabajador'}),
            'sueldo': forms.TextInput(attrs={'class': 'form-control', 'id': 'sueldo', 'placeholder': '3000 ejemplo'}),
            'position': forms.Select(attrs={'class': 'form-control', 'id': 'exampleFormControlSelect1'}),
        }
