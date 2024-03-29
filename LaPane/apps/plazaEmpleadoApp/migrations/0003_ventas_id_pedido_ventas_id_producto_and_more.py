# Generated by Django 4.0.1 on 2022-02-22 05:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plazaEmpleadoApp', '0002_alter_ventas_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='ventas',
            name='id_pedido',
            field=models.ForeignKey(blank=True, db_column='id_pedido', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='plazaEmpleadoApp.pedidos'),
        ),
        migrations.AddField(
            model_name='ventas',
            name='id_producto',
            field=models.ForeignKey(blank=True, db_column='id_producto', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='plazaEmpleadoApp.productos'),
        ),
        migrations.AlterField(
            model_name='ventas',
            name='fventa',
            field=models.DateTimeField(auto_now_add=True, db_column='fVenta'),
        ),
        migrations.AlterField(
            model_name='ventas',
            name='valortotal',
            field=models.DecimalField(db_column='valorTotal', decimal_places=2, max_digits=10),
        ),
    ]
