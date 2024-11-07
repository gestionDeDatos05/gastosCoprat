from django.shortcuts import render
from Aplicacion.models import *
from datetime import datetime

def editarCliente(request):
    id = request.POST['id'] # CAMPO id
    TECliente = tblCliente.objects.get(ID=id)
    return render(request, "Catalogo/Cliente/editar.html",{'TECliente': TECliente})

def editarFormaDePago(request):
    id = request.POST['id'] # CAMPO id
    TEFormaPago = tblFormaPago.objects.get(ID=id)
    return render(request, "Catalogo/FormaPago/editar.html",{'TEFormaPago': TEFormaPago})

def editarCategoria(request):
    id = request.POST['id'] # CAMPO id
    TECategoria = tblCategoriaGasto.objects.get(ID=id)
    return render(request, "Catalogo/TipoGasto/editar.html",{'TECategoria': TECategoria})

def editarAltaProyecto(request):
    id = request.POST['id'] # CAMPO id
    TEProyecto = tblAltaProyecto.objects.get(ID=id)
    FiltradoCliente = tblCliente.objects.get(ID = TEProyecto.IDCliente.ID)
    FiltradoEstatus = tblEstatus.objects.get(ID = TEProyecto.IDEstatus.ID)
    FechaInicio = TEProyecto.FechaInicio
    Fechafinal = TEProyecto.Fechafinal
    FECliente = tblCliente.objects.all()
    FEEstatus = tblEstatus.objects.all()
    return render(request, "Catalogo/Proyecto/editar.html",{'TEProyecto': TEProyecto, 'FiltradoCliente':FiltradoCliente, 'FECliente':FECliente,
                        'FechaInicio': FechaInicio, 'Fechafinal': Fechafinal, 'FiltradoEstatus': FiltradoEstatus, 'FEEstatus':FEEstatus})
