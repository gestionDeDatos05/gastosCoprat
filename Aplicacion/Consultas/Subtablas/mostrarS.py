from django.shortcuts import render, redirect
from Aplicacion.models import *
from django.contrib import messages
from datetime import datetime
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------SECCION DE DAR DE ALTA--------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def tablaEstatus(request):
    data = tblEstatus.objects.all()
    return render(request, 'Subtabla/Estatus/index.html', {"data": data})