# Generated by Django 4.0.1 on 2022-03-06 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plazaEmpleadoApp', '0012_alter_productosplaza_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedidos',
            name='id_pedido',
            field=models.AutoField(db_column='id_pedido', primary_key=True, serialize=False),
        ),
    ]