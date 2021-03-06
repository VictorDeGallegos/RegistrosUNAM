from django.db import models
from django.core.validators import MaxValueValidator
from django.core.validators import RegexValidator

# Create your models here.


class position(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class employee(models.Model):
    nombre_completo = models.CharField(max_length=100, validators=[
        RegexValidator(r'^[a-zA-Z ]{4,}(?: [a-zA-Z ]+){0,2}$',
                       message='Solo letras y al menos 4 letras para el NOMBRE COMPLETO')])
    CURP = models.CharField(max_length=18, unique=True, validators=[
        RegexValidator(r'^([A-Z][AEIOUX][A-Z]{2}\d{2}(?:0[1-9]|1[0-2])(?:0[1-9]|[12]\d|3[01])[HM](?:AS|B[CS]|C[CLMSH]|D[FG]|G[TR]|HG|JC|M[CNS]|N[ETL]|OC|PL|Q[TR]|S[PLR]|T[CSL]|VZ|YN|ZS)[B-DF-HJ-NP-TV-Z]{3}[A-Z\d])(\d)$',
                       message='Formato de CURP incorrecto')])
    direccion = models.CharField(max_length=200, )
    sueldo = models.CharField(max_length=5, validators=[
        RegexValidator(r'^\d{1,10}$',
                       message='Solo numeros para el SUELDO')])
    numero_de_empleado = models.CharField(max_length=10, unique=True, validators=[
        RegexValidator(r'^\d{1,10}$',
                       message='Solo numeros para el NUMERO DE EMPLEADO')])
    años_de_antiguedad = models.CharField(max_length=2, validators=[
        RegexValidator(r'^\d{1,10}$',
                       message='Solo numeros para indicar la ANTIGUEDAD')])
    email = models.EmailField(max_length=200, unique=True)
    puesto_administrativo = '1'
    ayudante = '2'
    profesor = '3'
    investigador = '4'
    PUESTOS = [
        (puesto_administrativo, 'ADMINISTRATIVO'),
        (ayudante, 'AYUDANTE'),
        (profesor, 'PROFESOR'),
        (investigador, 'INVESTIGADOR'),
    ]
    position = models.CharField(
        max_length=20,
        choices=PUESTOS,
        default=1,
    )
    # position = models.ForeignKey(position, on_delete=models.CASCADE)
    pregunta1 = models.CharField(max_length=200, null=True, blank=True)
    pregunta2 = models.CharField(max_length=200, null=True, blank=True)
    pregunta3 = models.CharField(max_length=200, null=True, blank=True)
    pregunta4 = models.CharField(max_length=200, null=True, blank=True)
    pregunta5 = models.CharField(max_length=200, null=True, blank=True)
    pregunta6 = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.nombre_completo
