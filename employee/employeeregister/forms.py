from django import forms
from .models import position
from .models import employee


class employeeForm(forms.ModelForm):

    class Meta:
        model = employee
        fields = ("nombre_completo", "CURP", "direccion",
                  "numero_de_empleado", "años_de_antiguedad", "email", "sueldo", "position")
        widgets = {
            'nombre_completo': forms.TextInput(attrs={'class': 'form-control', 'id': 'nombre_completo', 'placeholder': 'Ejemplo: Victor Hugo Gallegos Mota'}),
            'CURP': forms.TextInput(attrs={'class': 'form-control', 'id': 'CURP', 'placeholder': 'Ejemplo: GAMV991024HDFLTC01'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'id': 'direccion', 'placeholder': 'Ejemplo: Investigación Científica, C.U., Coyoacán, 04510 Ciudad de México, CDMX'}),
            'numero_de_empleado': forms.TextInput(attrs={'class': 'form-control', 'id': 'mobNo', 'placeholder': 'Ejemplo: 316160456'}),
            'años_de_antiguedad': forms.TextInput(attrs={'class': 'form-control', 'id': 'años_de_antiguedad', 'placeholder': 'Ejemplo: 3'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'id': 'email', 'placeholder': 'Ejemplo: admin@ciencias.unam.mx'}),
            'sueldo': forms.TextInput(attrs={'class': 'form-control', 'id': 'sueldo', 'placeholder': 'Ejemplo: 3000'}),
            'position': forms.Select(attrs={'class': 'form-control', 'id': 'exampleFormControlSelect1'}),
        }
