from django.shortcuts import render, redirect
from Aplicacion.models import *
from django.contrib import messages
from datetime import datetime

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------GUARDAR APARTADO DE ALTA-------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def guardarCliente(request):
    nombre = request.POST['nombre'].upper() # CAMPO CLIENTE
    areaTrabajo = request.POST['areaTrabajo']
    nombre_Existe = tblCliente.objects.filter(Nombre=nombre, IDAreaTrabajo = areaTrabajo).exists() # VALIDAR SI EL CLIENTE NO SE REGISTRO ANTERIORMENTE
    if nombre_Existe:
        messages.error(request, f'El cliente "{nombre}" ya ha sido registrado antreriormente') 
        if request.method == 'POST':
            if 'proyecto' in request.POST:
                return redirect('T_Clientes')
            elif 'mensuales' in request.POST:
                return redirect('TM_Clientes')
    else:
        tblCliente.objects.create(Nombre = nombre, IDAreaTrabajo_id = areaTrabajo)
        messages.success(request, f'El cliente {nombre} se ha registrado exitosamente')
        if request.method == 'POST':
            if 'proyecto' in request.POST:
                return redirect('T_Clientes')
            elif 'mensuales' in request.POST:
                return redirect('TM_Clientes')
    
def guardarFormaDePago(request):
    descripcion = request.POST['descripcion'].upper() # CAMPO DESCRIPCION
    areaTrabajo = request.POST['areaTrabajo']    
    nombre_Existe = tblFormaPago.objects.filter(Descripcion=descripcion, IDAreaTrabajo = areaTrabajo).exists() # VALIDAR SI EL CLIENTE NO SE REGISTRO ANTERIORMENTE
    if nombre_Existe:
        messages.error(request, f'El metodo de pago "{descripcion}" ya ha sido registrado antreriormente')        
        if request.method == 'POST':
            if 'proyecto' in request.POST:
                return redirect('T_Forma_de_pago')
            elif 'mensuales' in request.POST:
                return redirect('TM_Forma_de_pago')        
    else:
        tblFormaPago.objects.create(Descripcion = descripcion, IDAreaTrabajo_id = areaTrabajo)
        messages.success(request, f'El metodo de pago {descripcion} se ha registrado exitosamente')
        if request.method == 'POST':
            if 'proyecto' in request.POST:
                return redirect('T_Forma_de_pago')
            elif 'mensuales' in request.POST:
                return redirect('TM_Forma_de_pago')        

def guardarCategoria(request):
    descripcion = request.POST['descripcion'].upper() # CAMPO DESCRIPCION
    areaTrabajo = request.POST['areaTrabajo']    
    nombre_Existe = tblCategoriaGasto.objects.filter(Descripcion=descripcion).exists() # VALIDAR SI EL CLIENTE NO SE REGISTRO ANTERIORMENTE
    if nombre_Existe:
        messages.error(request, f'La categoria "{descripcion}" ya ha sido registrado antreriormente')        
        if request.method == 'POST':
            if 'proyecto' in request.POST:
                return redirect('T_Categoria')
            elif 'mensuales' in request.POST:
                return redirect('TM_Categoria')         
    else:
        tblCategoriaGasto.objects.create(Descripcion = descripcion, IDAreaTrabajo_id = areaTrabajo)
        messages.success(request, f'La categoria {descripcion} se ha registrado exitosamente')
        if request.method == 'POST':
            if 'proyecto' in request.POST:
                return redirect('T_Categoria')
            elif 'mensuales' in request.POST:
                return redirect('TM_Categoria')         

def guardarProyecto(request):
    Folio = request.POST['Folio'].upper() # CAMPO CLIENTE
    cliente = request.POST['cliente'] # CAMPO CLIENTE
    proyectos = request.POST['proyectos'].upper() # CAMPO CLIENTE
    Presupuesto = request.POST['presupuesto'] # CAMPO CLIENTE
    descripcion = request.POST['descripcion'] # CAMPO CLIENTE
    fechaInicio = request.POST['fechaInicio'] # CAMPO CLIENTE
    fechaFinal = request.POST['fechaFinal'] # CAMPO CLIENTE
    EstatusDefault = 1
    areaTrabajo = request.POST['areaTrabajo']    

    if isinstance(Presupuesto, str):
        Presupuesto = Presupuesto.replace(',', '')
    tblAltaProyecto.objects.create( Folio = Folio, IDEstatus_id = EstatusDefault, IDCliente_id = cliente, Proyecto = proyectos, 
    Descripcion = descripcion, FechaInicio = fechaInicio, Fechafinal = fechaFinal, Presupuesto =  Presupuesto, IDAreaTrabajo_id = areaTrabajo)
    messages.success(request, f'El proyecto {proyectos} se ha registrado exitosamente')
    if request.method == 'POST':
        if 'proyecto' in request.POST:
            return redirect('T_Proyecto')
        elif 'mensuales' in request.POST:
            return redirect('T_Mensual')        