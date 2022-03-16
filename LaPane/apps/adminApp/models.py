from pyexpat import model
from django.db import models
from ..userApp.models import Usuarios, Plazas
# Create your models here.

class Roles(models.Model):
    id_rol = models.AutoField(primary_key=True)
    tipoRol = models.CharField(db_column='tipoRol', max_length=8)
    class Meta:
        managed = True
        db_table = 'roles'
        
class Empleados(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuarios, models.DO_NOTHING, db_column='id_usuario', blank=True, null=True)
    id_plaza = models.ForeignKey(Plazas, models.DO_NOTHING, db_column='id_plaza', blank=True, null=True)
    id_rol = models.ForeignKey(Roles, models.DO_NOTHING, db_column='id_rol', blank=False, null=False)
    class Meta:
        managed = True
        db_table = 'empleados'