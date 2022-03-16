# Generated by Django 4.0.1 on 2022-03-16 04:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminApp', '0002_alter_empleados_options_alter_empleados_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id_rol', models.AutoField(primary_key=True, serialize=False)),
                ('tipoRol', models.CharField(choices=[('admin', 'admin'), ('empleado', 'empleado')], max_length=8)),
            ],
            options={
                'db_table': 'roles',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='empleados',
            name='id_rol',
            field=models.ForeignKey(blank=True, db_column='id_rol', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='adminApp.roles'),
        ),
    ]