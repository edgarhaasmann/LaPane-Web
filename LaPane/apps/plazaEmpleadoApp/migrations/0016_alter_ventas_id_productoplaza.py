# Generated by Django 4.0.1 on 2022-03-09 07:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plazaEmpleadoApp', '0015_pedidos_estadopago'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ventas',
            name='id_productoPlaza',
            field=models.ForeignKey(blank=True, db_column='id_producto', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='plazaEmpleadoApp.productosplaza'),
        ),
    ]