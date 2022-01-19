# Django
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
"""Users models."""


class Profile(models.Model):
    """Profile model.

    Proxy model that extends the base data with other
    information.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    NumeroTrabajador = models.CharField(max_length=20, blank=True)
    CURP = models.TextField(blank=True)
    Direccion = models.TextField(blank=True)
    Sueldo = models.CharField(max_length=20, blank=True)
    Antiguedad = models.CharField(max_length=20, blank=True)
    CorreoElectronico = models.CharField(max_length=200, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return username."""
        return self.user.username
