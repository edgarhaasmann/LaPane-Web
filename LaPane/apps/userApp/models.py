from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from datetime import datetime

class UsuarioManager(BaseUserManager):
    def create_user(self, nombre, appaterno, apmaterno, fnaciemiento, user, password):
        if not user:
            raise ValueError('No tiene usuario')
        usuario = self.model(
            nombre = nombre,
            appaterno = appaterno,
            apmaterno = apmaterno,
            fnaciemiento = fnaciemiento,
            user = user
        )
        usuario.set_password(password)
        usuario.save()
        return usuario
    def create_superuser(self, nombre, appaterno, apmaterno, fnaciemiento, user, password):
        usuario = self.create_user(
            nombre = nombre,
            appaterno = appaterno,
            apmaterno = apmaterno,
            fnaciemiento = fnaciemiento,
            user = user,
            password= password
        )
        usuario.save()
        return usuario

class Usuarios(AbstractBaseUser):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    appaterno = models.CharField(db_column='apPaterno', max_length=30)  # Field name made lowercase.
    apmaterno = models.CharField(db_column='apMaterno', max_length=30)  # Field name made lowercase.
    fnaciemiento = models.DateField(db_column='fNaciemiento')  # Field name made lowercase.
    user = models.CharField(unique=True, max_length=30)
    password = models.CharField(max_length=30)
    objects = UsuarioManager()
    

    USERNAME_FIELD = 'user'
    REQUIRED_FIELDS = ['nombre','appaterno','apmaterno','fnaciemiento']

    class Meta:
        managed = True
        db_table = 'usuarios'


class Plazas(models.Model):
    id_plaza = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    ubicacion = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'plazas'
 
    def __str__(self):
        return self.nombre




