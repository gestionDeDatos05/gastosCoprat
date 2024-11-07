from django.shortcuts import render, redirect
from Aplicacion.models import *
from django.contrib import messages
from datetime import datetime

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------GUARDAR APARTADO DE ALTA-------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def guardarCliente(request):
    nombre = request.POST['nombre'].upper() # CAMPO CLIENTE
    nombre_Existe = tblCliente.objects.filter(Nombre=nombre).exists() # VALIDAR SI EL CLIENTE NO SE REGISTRO ANTERIORMENTE
    if nombre_Existe:
        messages.error(request, f'El cliente "{nombre}" ya ha sido registrado antreriormente')        
        return redirect('T_Clientes')
    else:
        tblCliente.objects.create(Nombre = nombre)
        messages.success(request, f'El cliente {nombre} se ha registrado exitosamente')
        return redirect('T_Clientes')
    
def guardarFormaDePago(request):
    descripcion = request.POST['descripcion'].upper() # CAMPO DESCRIPCION
    nombre_Existe = tblFormaPago.objects.filter(Descripcion=descripcion).exists() # VALIDAR SI EL CLIENTE NO SE REGISTRO ANTERIORMENTE
    if nombre_Existe:
        messages.error(request, f'El metodo de pago "{descripcion}" ya ha sido registrado antreriormente')        
        return redirect('T_Forma_de_pago')
    else:
        tblFormaPago.objects.create(Descripcion = descripcion)
        messages.success(request, f'El metodo de pago {descripcion} se ha registrado exitosamente')
        return redirect('T_Forma_de_pago')

def guardarCategoria(request):
    descripcion = request.POST['descripcion'].upper() # CAMPO DESCRIPCION
    nombre_Existe = tblCategoriaGasto.objects.filter(Descripcion=descripcion).exists() # VALIDAR SI EL CLIENTE NO SE REGISTRO ANTERIORMENTE
    if nombre_Existe:
        messages.error(request, f'La categoria "{descripcion}" ya ha sido registrado antreriormente')        
        return redirect('T_Categoria')
    else:
        tblCategoriaGasto.objects.create(Descripcion = descripcion)
        messages.success(request, f'La categoria {descripcion} se ha registrado exitosamente')
        return redirect('T_Categoria')

def guardarProyecto(request):
    Folio = request.POST['Folio'].upper() # CAMPO CLIENTE
    cliente = request.POST['cliente'] # CAMPO CLIENTE
    proyecto = request.POST['proyecto'].upper() # CAMPO CLIENTE
    descripcion = request.POST['descripcion'] # CAMPO CLIENTE
    fechaInicio = request.POST['fechaInicio'] # CAMPO CLIENTE
    fechaFinal = request.POST['fechaFinal'] # CAMPO CLIENTE
    EstatusDefault = 1
    
    
    tblAltaProyecto.objects.create( Folio = Folio, IDEstatus_id = EstatusDefault, IDCliente_id = cliente, Proyecto = proyecto, 
    Descripcion = descripcion, FechaInicio = fechaInicio, Fechafinal = fechaFinal )
    messages.success(request, f'El proyecto {proyecto} se ha registrado exitosamente')
    return redirect('T_Proyecto')