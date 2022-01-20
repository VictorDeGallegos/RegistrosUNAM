from django import forms
from .models import position
from .models import employee


class employeeForm(forms.ModelForm):

    class Meta:
        model = employee
        fields = ("FullName", "CURP", "mobile_no", "emp_code", "position")
        widgets = {
            'FullName': forms.TextInput(attrs={'class': 'form-control', 'id': 'fullName', 'placeholder': 'Nombre Completo'}),
            'CURP': forms.TextInput(attrs={'class': 'form-control', 'id': 'CURP', 'placeholder': 'CURP'}),
            'mobile_no': forms.TextInput(attrs={'class': 'form-control', 'id': 'mobNo', 'placeholder': '# de trabajador'}),
            'emp_code': forms.TextInput(attrs={'class': 'form-control', 'id': 'emp_code', 'placeholder': '3000 ejemplo'}),
            'position': forms.Select(attrs={'class': 'form-control', 'id': 'exampleFormControlSelect1'}),
        }
