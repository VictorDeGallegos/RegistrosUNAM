from django.db import models
from django.core.validators import MaxValueValidator
from django.core.validators import RegexValidator

# Create your models here.


class position(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class employee(models.Model):
    nombre_completo = models.CharField(max_length=100)
    CURP = models.CharField(max_length=18, validators=[
        RegexValidator(r'^([A-Z][AEIOUX][A-Z]{2}\d{2}(?:0[1-9]|1[0-2])(?:0[1-9]|[12]\d|3[01])[HM](?:AS|B[CS]|C[CLMSH]|D[FG]|G[TR]|HG|JC|M[CNS]|N[ETL]|OC|PL|Q[TR]|S[PLR]|T[CSL]|VZ|YN|ZS)[B-DF-HJ-NP-TV-Z]{3}[A-Z\d])(\d)$')])
    direccion = models.CharField(max_length=200, )
    sueldo = models.CharField(max_length=5, validators=[
        RegexValidator(r'^\d{1,10}$')])
    numero_de_empleado = models.CharField(max_length=10, validators=[
        RegexValidator(r'^\d{1,10}$')])
    años_de_antiguedad = models.CharField(max_length=2, validators=[
        RegexValidator(r'^\d{1,10}$')])
    email = models.EmailField(max_length=200)
    position = models.ForeignKey(position, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_completo
