from django.shortcuts import render, redirect
from Aplicacion.models import *
from django.contrib import messages


def actualizarCliente(request):
    id = request.POST['id']
    nombre = request.POST['nombre'].upper().strip()
    
    nombre_existente = tblCliente.objects.filter(Nombre=nombre).exclude(ID=id).exists()
    if nombre_existente:
        messages.error(request, f'El Cliente "{nombre}" ya ha sido registrado anteriormente.')
        TECliente = tblCliente.objects.get(ID=id)
        return render(request, "Catalogo/Cliente/editar.html",{'TECliente': TECliente})
    else:
        cliente = tblCliente.objects.get(ID=id)
        cliente.Nombre = nombre
        cliente.save()
        messages.success(request, f'El Cliente "{nombre}" se ha actualizado exitosamente.')
    return redirect('T_Clientes')

def actualizarFormaDePago(request):
    id = request.POST['id']
    descripcion = request.POST['descripcion'].upper().strip()
    
    nombre_existente = tblFormaPago.objects.filter(Descripcion=descripcion).exclude(ID=id).exists()
    if nombre_existente:
        messages.error(request, f'La forma de pago "{descripcion}" ya ha sido registrado anteriormente.')
        TEFormaPago = tblFormaPago.objects.get(ID=id)
        return render(request, "Catalogo/FormaPago/editar.html",{'TEFormaPago': TEFormaPago})
    else:
        pago = tblFormaPago.objects.get(ID=id)
        pago.Descripcion = descripcion
        pago.save()
        messages.success(request, f'La forma de pago "{descripcion}" se ha actualizado exitosamente.')
    return redirect('T_Forma_de_pago')

def actualizarCategoria(request):
    id = request.POST['id']
    descripcion = request.POST['descripcion'].upper().strip()
    
    nombre_existente = tblCategoriaGasto.objects.filter(Descripcion=descripcion).exclude(ID=id).exists()
    if nombre_existente:
        messages.error(request, f'La categoria "{descripcion}" ya ha sido registrado anteriormente.')
        TECategoria = tblCategoriaGasto.objects.get(ID=id)
        return render(request, "Catalogo/TipoGasto/editar.html",{'TECategoria': TECategoria})
    else:
        categoria = tblCategoriaGasto.objects.get(ID=id)
        categoria.Descripcion = descripcion
        categoria.save()
        messages.success(request, f'La categoria "{descripcion}" se ha actualizado exitosamente.')
    return redirect('T_Categoria')

def actualizarAltaProyecto(request):
    id = request.POST['id'] # CAMPO CLIENTE
    Folio = request.POST['Folio'].upper() # CAMPO CLIENTE
    cliente = request.POST['cliente'] # CAMPO CLIENTE
    estatus = request.POST['estatus'] # CAMPO CLIENTE
    proyecto = request.POST['proyecto'].upper() # CAMPO CLIENTE
    descripcion = request.POST['descripcion'] # CAMPO CLIENTE
    fechaInicio = request.POST['fechaInicio'] # CAMPO CLIENTE
    fechaFinal = request.POST['fechaFinal'] # CAMPO CLIENTE
    presupuesto = request.POST['presupuesto'] # CAMPO CLIENTE
    
    actualizarAltaProyecto = tblAltaProyecto.objects.get(ID=id)
    estatus_instancia = tblEstatus.objects.get(ID=estatus)
    cliente_instancia = tblCliente.objects.get(ID=cliente)
    actualizarAltaProyecto.Folio = Folio
    actualizarAltaProyecto.IDEstatus = estatus_instancia
    actualizarAltaProyecto.IDCliente = cliente_instancia
    actualizarAltaProyecto.Proyecto = proyecto
    actualizarAltaProyecto.Presupuesto = presupuesto
    actualizarAltaProyecto.Descripcion = descripcion
    actualizarAltaProyecto.FechaInicio = fechaInicio
    actualizarAltaProyecto.Fechafinal = fechaFinal
    actualizarAltaProyecto.save()
    messages.success(request, f'El proyecto "{proyecto}" se ha actualizado exitosamente.')

    return redirect('T_Proyecto')