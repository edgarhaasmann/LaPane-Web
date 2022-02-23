from django.db import models
from ..userApp.models import *
from datetime import datetime

class Productos(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombreproducto = models.CharField(db_column='nombreProducto', unique=True, max_length=30)  # Field name made lowercase.
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places = 2)
    id_plaza = models.ForeignKey(Plazas, models.DO_NOTHING, db_column='id_plaza', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'productos'


class Pedidos(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    nombrecliente = models.CharField(db_column='nombreCliente', max_length=30)  # Field name made lowercase.
    cantidadproducto = models.IntegerField(db_column='cantidadProducto')  # Field name made lowercase.
    id_producto = models.ForeignKey(Productos, models.DO_NOTHING, db_column='id_producto', blank=True, null=True)
    id_plaza = models.ForeignKey(Plazas, models.DO_NOTHING, db_column='id_plaza', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pedidos'

    def __str__(self):
        return self.nombrecliente 


class Ventas(models.Model):
    id_venta = models.AutoField(primary_key=True)
    fventa = models.DateField( auto_now=True , db_column='fVenta')  # Field name made lowercase.
    valortotal = models.DecimalField(max_digits=10, decimal_places=2, db_column='valorTotal')  # Field name made lowercase.
    id_producto = models.ForeignKey(Productos, models.DO_NOTHING, db_column='id_producto', blank=True, null=True)
    id_pedido = models.ForeignKey(Pedidos, models.DO_NOTHING, db_column='id_pedido', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ventas'
