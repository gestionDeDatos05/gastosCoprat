from django.shortcuts import render, redirect
from Aplicacion.models import *
from django.contrib import messages
from datetime import datetime

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------GUARDAR APARTADO DE ALTA-------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def guardarEstatus(request):
    descripcion = request.POST['descripcion'].upper() # CAMPO DESCRIPCION
    nombre_Existe = tblEstatus.objects.filter(Descripcion=descripcion).exists() # VALIDAR SI EL CLIENTE NO SE REGISTRO ANTERIORMENTE
    if nombre_Existe:
        messages.error(request, f'El estatus "{descripcion}" ya ha sido registrado antreriormente')        
        return redirect('T_Estatus')
    else:
        tblEstatus.objects.create(Descripcion = descripcion)
        messages.success(request, f'El estatus {descripcion} se ha registrado exitosamente')
        return redirect('T_Estatus')