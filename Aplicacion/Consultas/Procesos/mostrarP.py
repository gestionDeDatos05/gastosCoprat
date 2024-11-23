from django.shortcuts import render, redirect
from Aplicacion.models import *
from django.contrib import messages
from datetime import datetime
from django.db.models import Sum
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------DETALLAR GASTOS DE PROYECTOS-----------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def detalleProyecto(request):
    id = request.POST['id'] # CAMPO id
    cliente = request.POST['cliente'] # CAMPO cliente
    proyecto = request.POST['proyecto'].upper() # CAMPO proyecto
    folio = request.POST['folio'] # CAMPO folio
    descripcion = request.POST['descripcion'] # CAMPO descripcion
    
    fecha_actual = datetime.now().date()
    fecha_formateada = fecha_actual.strftime('%Y-%m-%d') 
    selectPago = tblFormaPago.objects.filter(IDAreaTrabajo = 1)
    selectCategoria = tblCategoriaGasto.objects.filter(IDAreaTrabajo = 1)
    context = {'id':id, 'cliente': cliente, 'folio': folio, 'proyecto': proyecto, 'descripcion':descripcion}
    
    proveedor = tblProyecto.objects.filter(IDAreaTrabajo = 1).values("Proveedor").distinct()    
    detalleProyecto = tblProyecto.objects.filter(IDProyecto = id).values("ID", "IDProyecto_id__Folio", "Proveedor",
    "IDFormaDePago_id__Descripcion", "IDCategoria_id__Descripcion", "Monto", "Factura", "Descripcion", "Fecha").order_by('-Fecha')
    montoXCategoria = tblProyecto.objects.values('IDProyecto_id', 'IDCategoria_id__Descripcion').annotate(total_monto=Sum('Monto'))
    montoXPago = tblProyecto.objects.values('IDProyecto_id', 'IDFormaDePago_id__Descripcion').annotate(total_monto=Sum('Monto'))

        
    return render(request, 'Proceso/Gastos/index.html', {"context": context, 'selectPago':selectPago, 'selectCategoria':selectCategoria, 
    'fecha_actual':fecha_formateada, 'detalleProyecto':detalleProyecto, 'montoXCategoria':montoXCategoria,'montoXPago':montoXPago,
    'proveedor':proveedor})

def detalleGastos(request):
    id = request.POST['id'] # CAMPO id
    cliente = request.POST['cliente'] # CAMPO cliente
    proyecto = request.POST['proyecto'].upper() # CAMPO proyecto
    folio = request.POST['folio'] # CAMPO folio
    descripcion = request.POST['descripcion'] # CAMPO descripcion
    
    fecha_actual = datetime.now().date()
    fecha_formateada = fecha_actual.strftime('%Y-%m-%d') 
    selectPago = tblFormaPago.objects.filter(IDAreaTrabajo = 2)
    selectCategoria = tblCategoriaGasto.objects.filter(IDAreaTrabajo = 2)
    context = {'id':id, 'cliente': cliente, 'folio': folio, 'proyecto': proyecto, 'descripcion':descripcion}
    
    proveedor = tblProyecto.objects.filter(IDAreaTrabajo = 2).values("Proveedor").distinct()    
    detalleProyecto = tblProyecto.objects.filter(IDProyecto = id).values("ID", "IDProyecto_id__Folio", "Proveedor",
    "IDFormaDePago_id__Descripcion", "IDCategoria_id__Descripcion", "Monto", "Factura", "Descripcion", "Fecha").order_by('-Fecha')    
    montoXCategoria = tblProyecto.objects.values('IDProyecto_id', 'IDCategoria_id__Descripcion').annotate(total_monto=Sum('Monto'))
    montoXPago = tblProyecto.objects.values('IDProyecto_id', 'IDFormaDePago_id__Descripcion').annotate(total_monto=Sum('Monto'))

        
    return render(request, 'Proceso/Gastos/gastos.html', {"context": context, 'selectPago':selectPago, 'selectCategoria':selectCategoria, 
    'fecha_actual':fecha_formateada, 'detalleProyecto':detalleProyecto, 'montoXCategoria':montoXCategoria,'montoXPago':montoXPago,
    'proveedor':proveedor})