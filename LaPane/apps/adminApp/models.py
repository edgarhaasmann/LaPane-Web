from pyexpat import model
from django.db import models
from ..userApp.models import Usuarios, Plazas
# Create your models here.

class Empleados(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuarios, models.DO_NOTHING, db_column='id_usuario', blank=True, null=True)
    id_plaza = models.ForeignKey(Plazas, models.DO_NOTHING, db_column='id_plaza', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'empleados'