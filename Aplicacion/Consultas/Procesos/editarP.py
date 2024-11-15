from django.shortcuts import render
from Aplicacion.models import *
from datetime import datetime
from django.db.models import Sum

def editarProyecto(request):
    id = request.POST['id'] # CAMPO id
    TEProyecto = tblProyecto.objects.get(ID=id)
    FiltradoCategoria = tblCategoriaGasto.objects.get(ID = TEProyecto.IDCategoria.ID)
    FiltradoFormaPago = tblFormaPago.objects.get(ID = TEProyecto.IDFormaDePago.ID)
    areaTrabajo = TEProyecto.IDAreaTrabajo.ID
    Fecha = TEProyecto.Fecha
    proveedor = tblProyecto.objects.filter(IDAreaTrabajo = areaTrabajo).values("Proveedor").distinct()
    FECategoria = tblCategoriaGasto.objects.filter(IDAreaTrabajo = areaTrabajo)
    FEFormaPago = tblFormaPago.objects.filter(IDAreaTrabajo = areaTrabajo)
    
    #  DATOS PARA REGRESAR AL TEMPLATE DE PROYECTOS
    id_Proyecto = request.POST['idProyecto'] # CAMPO id
    cliente = request.POST['cliente'] # CAMPO cliente
    proyecto = request.POST['proyecto'].upper() # CAMPO proyecto
    folio = request.POST['folio'].upper() # CAMPO folio
    descripcion = request.POST['descripcionProyecto'] # CAMPO descripcion
    
    context = {'id':id_Proyecto, 'cliente': cliente, 'folio': folio, 'proyecto': proyecto, 'descripcion':descripcion}   
    return render(request, "Proceso/Gastos/editar.html",{"context": context, 'TEProyecto': TEProyecto, 'FiltradoCategoria':FiltradoCategoria, 'areaTrabajo':areaTrabajo, 
    'FiltradoFormaPago':FiltradoFormaPago, 'Fecha': Fecha, 'FECategoria': FECategoria, 'FEFormaPago': FEFormaPago, 'proveedor':proveedor})

def cancelarEditadoProyecto(request):
    id = request.POST['id'] # CAMPO id
    cliente = request.POST['cliente'] # CAMPO cliente
    proyecto = request.POST['proyecto'].upper() # CAMPO proyecto
    folio = request.POST['folio'].upper() # CAMPO folio
    descripcion = request.POST['descripcion'] # CAMPO descripcion
    
    fecha_actual = datetime.now().date()
    fecha_formateada = fecha_actual.strftime('%Y-%m-%d') 
    selectPago = tblFormaPago.objects.filter(IDAreaTrabajo = 1)
    selectCategoria = tblCategoriaGasto.objects.filter(IDAreaTrabajo = 1)
    context = {'id':id, 'cliente': cliente, 'folio': folio, 'proyecto': proyecto, 'descripcion':descripcion}
    
    detalleProyecto = tblProyecto.objects.filter(IDProyecto = id).values("ID", "IDProyecto_id__Folio", "Fecha",
    "IDFormaDePago_id__Descripcion", "IDCategoria_id__Descripcion", "Monto", "Factura", "Descripcion", "Proveedor")
    
    proveedor = tblProyecto.objects.values("Proveedor").distinct()

    montoXCategoria = tblProyecto.objects.values('IDProyecto_id', 'IDCategoria_id__Descripcion').annotate(total_monto=Sum('Monto'))
    montoXPago = tblProyecto.objects.values('IDProyecto_id', 'IDFormaDePago_id__Descripcion').annotate(total_monto=Sum('Monto'))

        
    return render(request, 'Proceso/Gastos/index.html', {"context": context, 'selectPago':selectPago, 'selectCategoria':selectCategoria, 
    'fecha_actual':fecha_formateada, 'detalleProyecto':detalleProyecto, 'montoXCategoria':montoXCategoria,'montoXPago':montoXPago,
    'proveedor':proveedor})
    
def cancelarEditadoMensuales(request):
    id = request.POST['id'] # CAMPO id
    cliente = request.POST['cliente'] # CAMPO cliente
    proyecto = request.POST['proyecto'].upper() # CAMPO proyecto
    folio = request.POST['folio'].upper() # CAMPO folio
    descripcion = request.POST['descripcion'] # CAMPO descripcion
    
    fecha_actual = datetime.now().date()
    fecha_formateada = fecha_actual.strftime('%Y-%m-%d') 
    selectPago = tblFormaPago.objects.filter(IDAreaTrabajo = 2)
    selectCategoria = tblCategoriaGasto.objects.filter(IDAreaTrabajo = 2)
    context = {'id':id, 'cliente': cliente, 'folio': folio, 'proyecto': proyecto, 'descripcion':descripcion}
    
    detalleProyecto = tblProyecto.objects.filter(IDProyecto = id).values("ID", "IDProyecto_id__Folio", "Fecha",
    "IDFormaDePago_id__Descripcion", "IDCategoria_id__Descripcion", "Monto", "Factura", "Descripcion", "Proveedor")
    
    proveedor = tblProyecto.objects.values("Proveedor").distinct()

    montoXCategoria = tblProyecto.objects.values('IDProyecto_id', 'IDCategoria_id__Descripcion').annotate(total_monto=Sum('Monto'))
    montoXPago = tblProyecto.objects.values('IDProyecto_id', 'IDFormaDePago_id__Descripcion').annotate(total_monto=Sum('Monto'))

        
    return render(request, 'Proceso/Gastos/gastos.html', {"context": context, 'selectPago':selectPago, 'selectCategoria':selectCategoria, 
    'fecha_actual':fecha_formateada, 'detalleProyecto':detalleProyecto, 'montoXCategoria':montoXCategoria,'montoXPago':montoXPago,
    'proveedor':proveedor})