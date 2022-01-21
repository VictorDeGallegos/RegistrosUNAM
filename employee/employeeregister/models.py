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
    CURP = models.CharField(max_length=18)
    direccion = models.CharField(max_length=200)
    sueldo = models.CharField(max_length=5)
    numero_de_empleado = models.CharField(max_length=10)
    años_de_antiguedad = models.CharField(max_length=2, validators=[
        RegexValidator(r'^\d{1,10}$')])
    email = models.EmailField(max_length=200)
    position = models.ForeignKey(position, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_completo
