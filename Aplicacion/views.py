from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from datetime import datetime
from django.db.models import Sum

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------VISTA PRICIPAL HOME O INCIIO-----------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def inicio(request):
    categoria = tblCategoriaGasto.objects.all()
    # Obtener la lista de proyectos con los campos deseados
    proyectos = tblAltaProyecto.objects.filter(IDEstatus_id = 1).values("ID", "Folio", "IDEstatus_id__Descripcion", "IDCliente_id__Nombre", "Proyecto", "Descripcion", "FechaInicio", "Fechafinal")

    fecha_actual = datetime.now().date()
    
    proyectos_con_dias = []  # Lista para almacenar los proyectos con días calculados

    montoXProyecto = tblProyecto.objects.values('IDProyecto_id').annotate(total_monto=Sum('Monto'))
    
    for proyecto in proyectos:
        fecha_inicial = proyecto['FechaInicio']
        fecha_final = proyecto['Fechafinal']    
        dias_totales = (fecha_final - fecha_inicial).days
        dias_restantes = (fecha_actual - fecha_inicial).days
        dias_para_porcentaje = (fecha_final - fecha_actual).days
        

        porcentaje_acumulado = ((dias_totales - dias_para_porcentaje) / dias_totales) * 100 if dias_totales > 0 else 0
        procentaje = int(porcentaje_acumulado)

        # Crear un nuevo diccionario con toda la información
        proyecto_info = {
            "ID": proyecto['ID'],
            "Folio": proyecto['Folio'],
            "IDEstatus_id__Descripcion": proyecto['IDEstatus_id__Descripcion'],
            "IDCliente_id__Nombre": proyecto['IDCliente_id__Nombre'],
            "Proyecto": proyecto['Proyecto'],
            "Descripcion": proyecto['Descripcion'],
            "FechaInicio": proyecto['FechaInicio'],
            "Fechafinal": proyecto['Fechafinal'],
            "DiasTotales": dias_totales,
            "DiasRestantes": dias_restantes,
            "porcentaje_acumulado": procentaje,
        }

        # Añadir el diccionario a la lista
        proyectos_con_dias.append(proyecto_info)
        
    fecha_actual = datetime.now().date()
    fecha_formateada = fecha_actual.strftime('%Y-%m-%d') 
    selectPago = tblFormaPago.objects.all()
    selectCategoria = tblCategoriaGasto.objects.all()
    selectProyecto = tblAltaProyecto.objects.filter(IDEstatus_id = 1)
    proveedor = tblProyecto.objects.values("Proveedor").distinct()    
    return render(request, 'include/index.html', {'categoria': categoria, 'proyectos': proyectos_con_dias, 'montoXProyecto':montoXProyecto,
    'selectPago':selectPago, 'selectCategoria':selectCategoria, 'fecha_actual':fecha_formateada, 'selectProyecto':selectProyecto, 'proveedor':proveedor})





