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
    proyectos = tblAltaProyecto.objects.all().values("ID", "Folio", "IDEstatus_id__Descripcion", "IDCliente_id__Nombre", "Proyecto", "Descripcion", "FechaInicio", "Fechafinal", "GastoTotal")

    fecha_actual = datetime.now().date()
    
    proyectos_con_dias = []  # Lista para almacenar los proyectos con días calculados

    montoXProyecto = tblProyecto.objects.values('IDProyecto_id').annotate(total_monto=Sum('Monto'))
    
    for proyecto in proyectos:
        fecha_inicial = proyecto['FechaInicio']
        fecha_final = proyecto['Fechafinal']    
        dias_totales = (fecha_final - fecha_inicial).days
        dias_restantes = (fecha_final - fecha_actual).days

        porcentaje_acumulado = ((dias_totales - dias_restantes) / dias_totales) * 100 if dias_totales > 0 else 0
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
    
    return render(request, 'include/index.html', {'categoria': categoria, 'proyectos': proyectos_con_dias, 'montoXProyecto':montoXProyecto})





