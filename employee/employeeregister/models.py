from django.db import models

# Create your models here.


class position(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class employee(models.Model):
    NombreCompleto = models.CharField(max_length=100)
    CURP = models.CharField(max_length=18)
    sueldo = models.CharField(max_length=9)
    mobile_no = models.CharField(max_length=10)
    position = models.ForeignKey(position, on_delete=models.CASCADE)

    def __str__(self):
        return self.NombreCompleto
