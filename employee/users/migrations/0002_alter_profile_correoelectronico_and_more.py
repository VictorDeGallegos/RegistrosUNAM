# Generated by Django 4.0.1 on 2022-01-23 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='CorreoElectronico',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='profile',
            name='NumeroTrabajador',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
