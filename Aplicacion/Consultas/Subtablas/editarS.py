from django.shortcuts import render
from Aplicacion.models import *

def editarEstatus(request):
    id = request.POST['id'] # CAMPO id
    data = tblEstatus.objects.get(ID=id)
    return render(request, 'Subtabla/Estatus/editar.html', {"data": data})