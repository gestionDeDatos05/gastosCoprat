from django.shortcuts import render, redirect
from Aplicacion.models import *
from django.contrib import messages
from datetime import datetime
from django.db.models import Sum
from django.db import connection
import mysql.connector
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------DETALLAR GASTOS DE PROYECTOS-----------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def reportesProyecto(request):
    # obtener los datos para el formulario de los reportes
    fecha_actual = datetime.now().date()
    fecha_formateada = fecha_actual.strftime('%Y-%m-%d') 
    selectProyecto = tblAltaProyecto.objects.filter(IDEstatus_id = 1)
    selectPago = tblFormaPago.objects.filter(IDAreaTrabajo = 1)
    selectCategoria = tblCategoriaGasto.objects.filter(IDAreaTrabajo = 1)   
    proveedor = tblProyecto.objects.values("Proveedor").distinct()    
    
    detalleProyecto = [] 

    if request.method == 'POST':
        proyecto_v = request.POST.get('proyecto')
        categoria_v = request.POST.get('categoria')
        pago_v = request.POST.get('pago')
        proveedor_v = request.POST.get('proveedor')
        factura_v = request.POST.get('factura')
        fechaI_v = request.POST.get('fechaI')
        fechaF_v = request.POST.get('fechaF')
        
        # Consulta los datos necesarios solo si no son "todos"
        proyecto_reporte = tblAltaProyecto.objects.get(ID=proyecto_v) if proyecto_v != "todos" else None
        categoria_reporte = tblCategoriaGasto.objects.get(ID=categoria_v) if categoria_v != "todos" else None
        pago_reporte = tblFormaPago.objects.get(ID=pago_v) if pago_v != "todos" else None

        conditions = []
        params = []

        if proyecto_v != "todos":
            conditions.append("Aplicacion_tblProyecto.IDProyecto_id = %s")
            params.append(proyecto_v)
            
        if categoria_v != "todos":
            conditions.append("Aplicacion_tblProyecto.IDCategoria_id = %s")
            params.append(categoria_v)

        if pago_v != "todos":
            conditions.append("Aplicacion_tblProyecto.IDFormaDePago_id = %s")
            params.append(pago_v)

        if factura_v == "Con factura":
            conditions.append("Aplicacion_tblProyecto.Factura != 'SF'")

        elif factura_v == "Sin factura":
            conditions.append("Aplicacion_tblProyecto.Factura = 'SF'")

        if proveedor_v != "Todos los proveedores":
            conditions.append("Aplicacion_tblProyecto.Proveedor = %s")
            params.append(proveedor_v)

        # Añadir condición de fecha siempre
        conditions.append("Aplicacion_tblProyecto.Fecha BETWEEN %s AND %s ")
        params.extend([fechaI_v, fechaF_v])

        # Construir la consulta final uniendo las condiciones con " AND "
        where_clause = " AND ".join(conditions)
        consulta_sql = f"""SELECT DISTINCT Aplicacion_tblProyecto.Fecha, Aplicacion_tblAltaProyecto.Folio, Aplicacion_tblAltaProyecto.Proyecto, Aplicacion_tblFormaPago.Descripcion,
            Aplicacion_tblProyecto.Monto, Aplicacion_tblProyecto.Factura, Aplicacion_tblCategoriaGasto.Descripcion, Aplicacion_tblProyecto.Descripcion, Aplicacion_tblProyecto.Proveedor,
            Aplicacion_tblCliente.Nombre
            FROM Aplicacion_tblProyecto
            LEFT JOIN Aplicacion_tblAltaProyecto ON Aplicacion_tblProyecto.IDProyecto_id = Aplicacion_tblAltaProyecto.ID
            LEFT JOIN Aplicacion_tblCliente ON Aplicacion_tblAltaProyecto.IDCliente_id = Aplicacion_tblCliente.ID
            LEFT JOIN Aplicacion_tblFormaPago ON Aplicacion_tblProyecto.IDFormaDePago_id = Aplicacion_tblFormaPago.ID
            LEFT JOIN Aplicacion_tblCategoriaGasto ON Aplicacion_tblProyecto.IDCategoria_id = Aplicacion_tblCategoriaGasto.ID
            WHERE {where_clause} AND Aplicacion_tblAltaProyecto.IDEstatus_id = 1
        """
        # Ejecutar la consulta
        with connection.cursor() as cursor:
            cursor.execute(consulta_sql, params)
            reportes = cursor.fetchall()
            
        consulta_sql_total = f""" SELECT SUM(Aplicacion_tblProyecto.Monto) AS TotalMonto FROM Aplicacion_tblProyecto
        LEFT JOIN Aplicacion_tblAltaProyecto ON Aplicacion_tblProyecto.IDProyecto_id = Aplicacion_tblAltaProyecto.ID
        WHERE {where_clause} AND Aplicacion_tblAltaProyecto.IDEstatus_id = 1"""
        with connection.cursor() as cursor:
            cursor.execute(consulta_sql_total, params)
            suma_Total = cursor.fetchall()
            
        context = {
            'proyecto_reporte': proyecto_reporte,
            'categoria_reporte': categoria_reporte,
            'pago_reporte': pago_reporte,
            'factura_reporte': factura_v,
            'proveedor_reporte': proveedor_v,
            'fechaI_reporte': fechaI_v,
            'fechaF_reporte': fechaF_v,
            'selectPago': selectPago,
            'selectCategoria': selectCategoria,
            'detalleProyecto': reportes,
            'proveedor': proveedor,
            'fecha_actual': fecha_formateada,
            'selectProyecto': selectProyecto,
            'suma_Total':suma_Total
        }

        return render(request, 'Reporte/index.html', context)
    
    return render(request, 'Reporte/index.html', {'selectPago':selectPago, 'selectCategoria':selectCategoria,
    'detalleProyecto':detalleProyecto, 'proveedor':proveedor, 'fecha_actual':fecha_formateada, 'selectProyecto':selectProyecto})
