from django.db import models

# Create your models here.

# SUBRTABLAS
class tblEstatus(models.Model):
    ID = models.AutoField(primary_key=True)
    Descripcion = models.CharField(max_length=30, null=True)
    
# CATALOGOS
class tblCliente(models.Model):
    ID = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=50, null=True)
    
class tblAltaProyecto(models.Model):
    ID = models.AutoField(primary_key=True)
    Folio = models.CharField(max_length=30, null=True)
    IDEstatus = models.ForeignKey(tblEstatus, on_delete=models.DO_NOTHING, null=True)
    IDCliente = models.ForeignKey(tblCliente, on_delete=models.DO_NOTHING, null=True)
    Proyecto = models.CharField(max_length=60, null=True)
    Presupuesto = models.FloatField(null=True)
    Descripcion = models.CharField(max_length=100, null=True)
    FechaInicio = models.DateField(null=True)
    Fechafinal = models.DateField(null=True)
    
class tblFormaPago(models.Model):
    ID = models.AutoField(primary_key=True)
    Descripcion = models.CharField(max_length=30, null=True)

class tblCategoriaGasto(models.Model):
    ID = models.AutoField(primary_key=True)
    Descripcion = models.CharField(max_length = 30, null=True)
    
# PROYECTO
class tblProyecto(models.Model):
    ID = models.AutoField(primary_key=True)
    IDProyecto = models.ForeignKey(tblAltaProyecto, on_delete=models.DO_NOTHING, null=True)
    IDFormaDePago = models.ForeignKey(tblFormaPago, on_delete=models.DO_NOTHING, null=True)
    IDCategoria = models.ForeignKey(tblCategoriaGasto, on_delete=models.DO_NOTHING, null=True)
    Monto = models.FloatField(null=True)
    Factura = models.CharField(max_length=60, null=True)
    Descripcion = models.CharField(max_length=100, null=True)
    Proveedor = models.CharField(max_length=100, null=True)
    Fecha = models.DateField(null=True)