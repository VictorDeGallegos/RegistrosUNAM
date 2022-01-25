# Generated by Django 4.0.1 on 2022-01-25 20:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeeregister', '0005_alter_employee_curp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='numero_de_empleado',
            field=models.CharField(max_length=10, unique=True, validators=[django.core.validators.RegexValidator('^\\d{1,10}$', message='Solo numeros para el NUMERO DE EMPLEADO')]),
        ),
    ]