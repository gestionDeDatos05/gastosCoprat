from django.shortcuts import render, redirect
from Aplicacion.models import *
from django.contrib import messages
from datetime import datetime
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------SECCION DE DAR DE ALTA--------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def tablaCliente(request):
    data = tblCliente.objects.all()
    return render(request, 'Catalogo/Cliente/index.html', {"data": data})

def tablaFormaDePago(request):
    data = tblFormaPago.objects.all()
    return render(request, 'Catalogo/FormaPago/index.html', {"data": data})

def tablaCategoria(request):
    data = tblCategoriaGasto.objects.all()
    return render(request, 'Catalogo/TipoGasto/index.html', {"data": data})

def tablaProyecto(request):
    cliente = tblCliente.objects.all()
    fecha_actual = datetime.now().date()
    fecha_formateada = fecha_actual.strftime('%Y-%m-%d') 
    data = tblAltaProyecto.objects.all().values("ID", "Folio", "IDEstatus_id__Descripcion","IDCliente_id", "IDCliente_id__Nombre", "Proyecto", "Descripcion", "FechaInicio", "Fechafinal", "GastoTotal")
    return render(request, 'Catalogo/Proyecto/index.html', {"data": data, 'cliente':cliente, 'fecha_actual':fecha_formateada})
