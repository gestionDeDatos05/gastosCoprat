from django.shortcuts import render, redirect
from Aplicacion.models import *
from django.contrib import messages
from datetime import datetime
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------SECCION DE DAR DE ALTA--------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def tablaCliente(request):
    data = tblCliente.objects.filter(IDAreaTrabajo = 1)
    return render(request, 'Catalogo/Cliente/index.html', {"data": data})

def tablaFormaDePago(request):
    data = tblFormaPago.objects.filter(IDAreaTrabajo = 1)
    return render(request, 'Catalogo/FormaPago/index.html', {"data": data})

def tablaCategoria(request):
    data = tblCategoriaGasto.objects.filter(IDAreaTrabajo = 1)
    return render(request, 'Catalogo/TipoGasto/index.html', {"data": data})

def tablaProyecto(request):
    cliente = tblCliente.objects.filter(IDAreaTrabajo = 1)
    fecha_actual = datetime.now().date()
    fecha_formateada = fecha_actual.strftime('%Y-%m-%d') 
    data = tblAltaProyecto.objects.filter(IDAreaTrabajo = 1).values("ID", "Folio","IDEstatus_id", "IDEstatus_id__Descripcion","IDCliente_id", "IDCliente_id__Nombre", "Proyecto", "Descripcion", "FechaInicio", "Fechafinal", "Presupuesto")
    return render(request, 'Catalogo/Proyecto/index.html', {"data": data, 'cliente':cliente, 'fecha_actual':fecha_formateada})

def tablaClienteMensuales(request):
    data = tblCliente.objects.filter(IDAreaTrabajo = 2)
    return render(request, 'Catalogo/Cliente/gastos.html', {"data": data})

def tablaFormaDePagoMensuales(request):
    data = tblFormaPago.objects.filter(IDAreaTrabajo = 2)
    return render(request, 'Catalogo/FormaPago/gastos.html', {"data": data})

def tablaCategoriaMensuales(request):
    data = tblCategoriaGasto.objects.filter(IDAreaTrabajo = 2)
    return render(request, 'Catalogo/TipoGasto/gastos.html', {"data": data})

def tablaProyectoMensuales(request):
    cliente = tblCliente.objects.filter(IDAreaTrabajo = 2)
    fecha_actual = datetime.now().date()
    fecha_formateada = fecha_actual.strftime('%Y-%m-%d') 
    data = tblAltaProyecto.objects.filter(IDAreaTrabajo = 2).values("ID", "Folio","IDEstatus_id", "IDEstatus_id__Descripcion","IDCliente_id", "IDCliente_id__Nombre", "Proyecto", "Descripcion", "FechaInicio", "Fechafinal", "Presupuesto")
    return render(request, 'Catalogo/Proyecto/gastos.html', {"data": data, 'cliente':cliente, 'fecha_actual':fecha_formateada})
