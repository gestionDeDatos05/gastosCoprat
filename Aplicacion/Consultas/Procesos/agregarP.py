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
    factura = request.POST['factura'].upper() # CAMPO CLIENTE
    monto = request.POST['monto'] # CAMPO CLIENTE
    descripcion = request.POST['descripcion'].capitalize() # CAMPO CLIENTE
    proveedor = request.POST['proveedor'].upper() # CAMPO CLIENTE
    fecha = request.POST['fecha'] # CAMPO CLIENTE
    areaTrabajo = request.POST['areaTrabajo']    
    
    if isinstance(monto, str):
        monto = monto.replace(',', '')
        
    # REGRESA AL FORMULARIO LOS DATOS POR DEFECTOS, PARA LOS CAMPOS SELECT
    fecha_actual = datetime.now().date()
    fecha_formateada = fecha_actual.strftime('%Y-%m-%d') 
    selectPago = tblFormaPago.objects.filter(IDAreaTrabajo = areaTrabajo)
    selectCategoria = tblCategoriaGasto.objects.filter(IDAreaTrabajo = areaTrabajo)
    proveedorSearch = tblProyecto.objects.filter(IDAreaTrabajo = 1).values("Proveedor").distinct()
    nombreProyect = tblAltaProyecto.objects.get(ID  = idProyecto)
    FProyecto = nombreProyect.Folio
    NProyecto = nombreProyect.Proyecto
    
    tblProyecto.objects.create(IDProyecto_id = idProyecto, IDFormaDePago_id = pago, IDCategoria_id = categoria, 
    Monto = monto, Factura = factura, Descripcion = descripcion, Proveedor = proveedor, Fecha = fecha, IDAreaTrabajo_id = areaTrabajo)
    messages.success(request, f'Se ha registrado el monto $ {monto}, en el proyecto {FProyecto} - {NProyecto} exitosamente ')
    
    if request.method == 'POST':
        if 'inicio' in request.POST:
            return redirect('T_Inicio')
        elif 'gastos' in request.POST:
            return redirect('Mensual')
        else:
            # REGRESA AL FORMULARIO LOS DATOS SELECCIOANDOS ANTERIORMENTE
            id = request.POST['idProyecto'] # CAMPO id
            cliente = request.POST['cliente'] # CAMPO cliente
            proyecto = request.POST['proyecto'].upper() # CAMPO proyecto
            folio = request.POST['folio'] # CAMPO folio
            descripcionProyecto = request.POST['descripcionProyecto'] # CAMPO descripcion
            context = {'id':id, 'cliente': cliente, 'folio': folio, 'proyecto': proyecto, 'descripcion':descripcionProyecto}
            detalleProyecto = tblProyecto.objects.filter(IDProyecto = id).values("IDProyecto_id__Folio", "IDFormaDePago_id__Descripcion", 
                                        "IDCategoria_id__Descripcion", "Monto", "Factura", "Descripcion", "Proveedor", "Fecha")

            montoXCategoria = tblProyecto.objects.values('IDProyecto_id', 'IDCategoria_id__Descripcion').annotate(total_monto=Sum('Monto'))
            montoXPago = tblProyecto.objects.values('IDProyecto_id', 'IDFormaDePago_id__Descripcion').annotate(total_monto=Sum('Monto'))           
                
            return render(request, 'Proceso/Gastos/index.html', {"context": context, 'selectPago':selectPago, 'selectCategoria':selectCategoria, 
            'fecha_actual':fecha_formateada,'detalleProyecto':detalleProyecto, 'montoXCategoria':montoXCategoria,'montoXPago':montoXPago,
            'proveedor':proveedorSearch})