# Generated by Django 4.0.1 on 2022-03-06 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plazaEmpleadoApp', '0013_alter_pedidos_id_pedido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedidos',
            name='id_pedido',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
