# Generated by Django 4.0.1 on 2022-01-26 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeeregister', '0007_alter_employee_email_alter_employee_nombre_completo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='position',
            field=models.CharField(choices=[('1', 'ADMINISTRATIVO'), ('2', 'AYUDANTE'), ('3', 'PROFESOR'), ('4', 'INVESTIGADOR')], default=1, max_length=20),
        ),
    ]