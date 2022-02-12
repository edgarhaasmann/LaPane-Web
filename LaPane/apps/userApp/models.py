from django.db import models
from datetime import datetime

class Pedidos(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    nombrecliente = models.CharField(db_column='nombreCliente', max_length=30)  # Field name made lowercase.
    cantidadproducto = models.IntegerField(db_column='cantidadProducto')  # Field name made lowercase.
    id_producto = models.ForeignKey('Productos', models.DO_NOTHING, db_column='id_producto', blank=True, null=True)
    id_plaza = models.ForeignKey('Plazas', models.DO_NOTHING, db_column='id_plaza', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pedidos'

    def __str__(self):
        return self.nombrecliente 

class Plazas(models.Model):
    id_plaza = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    ubicacion = models.CharField(unique=True, max_length=30)
    id_usuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='id_usuario', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plazas'
    def __str__(self):
        return self.nombre

class Productos(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombreproducto = models.CharField(db_column='nombreProducto', unique=True, max_length=30)  # Field name made lowercase.
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places = 2)
    created_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now_add=True)
    id_plaza = models.ForeignKey(Plazas, models.DO_NOTHING, db_column='id_plaza', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'productos'
    def __str__(self):
        return self.nombreproducto

class Roles(models.Model):
    id_rol = models.AutoField(primary_key=True)
    tiporol = models.CharField(db_column='tipoRol', max_length=8)  # Field name made lowercase.
    id_usuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='id_usuario', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roles'


class Usuarios(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    appaterno = models.CharField(db_column='apPaterno', max_length=30)  # Field name made lowercase.
    apmaterno = models.CharField(db_column='apMaterno', max_length=30)  # Field name made lowercase.
    fnaciemiento = models.DateField(db_column='fNaciemiento')  # Field name made lowercase.
    user = models.CharField(unique=True, max_length=30)
    password = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        managed = False
        db_table = 'usuarios'

class Ventas(models.Model):
    id_venta = models.AutoField(primary_key=True)
    fventa = models.DateTimeField( auto_now=True , db_column='fVenta')  # Field name made lowercase.
    valortotal = models.FloatField(db_column='valorTotal')  # Field name made lowercase.
    id_producto = models.ForeignKey(Productos, models.DO_NOTHING, db_column='id_producto', blank=True, null=True)
    id_pedido = models.ForeignKey(Pedidos, models.DO_NOTHING, db_column='id_pedido', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ventas'
