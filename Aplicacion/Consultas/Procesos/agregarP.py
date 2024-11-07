from django.shortcuts import render, redirect
from Aplicacion.models import *
from django.contrib import messages
from datetime import datetime
from django.db.models import Sum

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------GUARDAR DETALLE GASTOS DE PROYECTOS----------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def guardarDetalleProyecto(request):
    idProyecto = request.POST['idProyecto'] # CAMPO CLIENTE
    categoria = request.POST['categoria'] # CAMPO CLIENTE
    pago = request.POST['pago'].upper() # CAMPO CLIENTE
    factura = request.POST['factura'] # CAMPO CLIENTE
    monto = request.POST['monto'] # CAMPO CLIENTE
    descripcion = request.POST['descripcion'] # CAMPO CLIENTE
    proveedor = request.POST['proveedor'].upper() # CAMPO CLIENTE
    fecha = request.POST['fecha'] # CAMPO CLIENTE
    
    # REGRESA AL FORMULARIO LOS DATOS SELECCIOANDOS ANTERIORMENTE
    id = request.POST['idProyecto'] # CAMPO id
    cliente = request.POST['cliente'] # CAMPO cliente
    proyecto = request.POST['proyecto'].upper() # CAMPO proyecto
    folio = request.POST['folio'] # CAMPO folio
    descripcionProyecto = request.POST['descripcionProyecto'] # CAMPO descripcion
    context = {'id':id, 'cliente': cliente, 'folio': folio, 'proyecto': proyecto, 'descripcion':descripcionProyecto}
    fecha_actual = datetime.now().date()
    fecha_formateada = fecha_actual.strftime('%Y-%m-%d') 
    selectPago = tblFormaPago.objects.all()
    selectCategoria = tblCategoriaGasto.objects.all()
    
    detalleProyecto = tblProyecto.objects.filter(IDProyecto = id).values("IDProyecto_id__Folio", "IDFormaDePago_id__Descripcion", 
                                "IDCategoria_id__Descripcion", "Monto", "Factura", "Descripcion", "Proveedor", "Fecha")

    proveedorSearch = tblProyecto.objects.values("Proveedor").distinct()

    montoXCategoria = tblProyecto.objects.values('IDProyecto_id', 'IDCategoria_id__Descripcion').annotate(total_monto=Sum('Monto'))
    montoXPago = tblProyecto.objects.values('IDProyecto_id', 'IDFormaDePago_id__Descripcion').annotate(total_monto=Sum('Monto'))
    
    tblProyecto.objects.create(IDProyecto_id = idProyecto, IDFormaDePago_id = pago, IDCategoria_id = categoria, 
    Monto = monto, Factura = factura, Descripcion = descripcion, Proveedor = proveedor, Fecha = fecha)
    messages.success(request, f'El monto $ {monto} se ha registrado exitosamente')
    
    return render(request, 'Proceso/Gastos/index.html', {"context": context, 'selectPago':selectPago, 'selectCategoria':selectCategoria, 
    'fecha_actual':fecha_formateada,'detalleProyecto':detalleProyecto, 'montoXCategoria':montoXCategoria,'montoXPago':montoXPago,
    'proveedor':proveedorSearch})