# Generated by Django 5.1.2 on 2024-11-21 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicacion', '0008_alter_tblaltaproyecto_presupuesto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tblproyecto',
            name='Monto',
            field=models.CharField(max_length=20, null=True),
        ),
    ]