# Generated by Django 2.2.11 on 2020-12-02 11:10

from django.db import migrations, models
import django.db.models.deletion
from django.core.validators import MaxValueValidator
from django.core.validators import RegexValidator


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='position',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_completo', models.CharField(max_length=100)),
                ('CURP', models.CharField(max_length=18)),
                ('direccion', models.CharField(max_length=200)),
                ('sueldo', models.CharField(max_length=5)),
                ('numero_de_empleado', models.CharField(max_length=10)),
                ('años_de_antiguedad', models.CharField(max_length=2,
                 validators=[RegexValidator(r'^\d{1,10}$')])),
                ('position', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='employeeregister.position')),
            ],
        ),
    ]
