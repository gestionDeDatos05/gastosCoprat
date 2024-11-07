from django.shortcuts import render, redirect
from Aplicacion.models import *
from django.contrib import messages

def actualizarEstatus(request):
    id = request.POST['id']
    descripcion = request.POST['descripcion'].upper().strip()
    
    nombre_existente = tblEstatus.objects.filter(Descripcion=descripcion).exclude(ID=id).exists()
    if nombre_existente:
        messages.error(request, f'El estatus "{descripcion}" ya ha sido registrado anteriormente.')
        data = tblEstatus.objects.get(ID=id)
        return render(request, "Subtabla/Estatus/editar.html",{'data': data})
    else:
        pago = tblEstatus.objects.get(ID=id)
        pago.Descripcion = descripcion
        pago.save()
        messages.success(request, f'El estatus "{descripcion}" se ha actualizado exitosamente.')
    return redirect('T_Estatus')