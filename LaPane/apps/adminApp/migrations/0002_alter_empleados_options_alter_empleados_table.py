# Generated by Django 4.0.1 on 2022-03-10 05:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='empleados',
            options={'managed': True},
        ),
        migrations.AlterModelTable(
            name='empleados',
            table='empleados',
        ),
    ]