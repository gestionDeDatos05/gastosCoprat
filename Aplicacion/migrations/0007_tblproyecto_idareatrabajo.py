# Generated by Django 5.1.2 on 2024-11-15 20:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicacion', '0006_tblareadetrabajo_tblaltaproyecto_idareatrabajo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tblproyecto',
            name='IDAreaTrabajo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Aplicacion.tblareadetrabajo'),
        ),
    ]
