from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from datetime import datetime
from django.db.models import Sum
# LLAMAR ARCHIVOS LOCALES
from django.contrib.auth.models import Group
from .forms import *
from .models import *
import logging
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< FUNCION REGISTRO DE USUARIOS >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
class CustomLoginView(LoginView):
    template_name = 'Acceso/login.html'
    def form_invalid(self, form):
        messages.error(self.request, 'Usuario o contraseña incorrectos.')
        return super().form_invalid(form)

# ------------------------------------------------------------REGISTRO-------------------------------------------------------------
def Register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            ultimo_usuario = User.objects.latest('id')
            default_group = Group.objects.get(name='Usuario')
            ultimo_usuario.groups.add(default_group)
            
            username = form.cleaned_data['username']
            first_name = request.POST['first_name'].title().strip()
            last_name = request.POST['last_name'].title().strip()
            messages.success(request, f'El Usuario con el email "{username}" ha sido creado')
            return redirect('Login')
        else:
            errors = form.errors
            print(errors) 
            username_errors = form.errors.get('username')
            if username_errors:
                username_error = username_errors[0]
                messages.error(request, f'Error en el campo "email". Error: Ya existe un usuario con ese email')
            else:
                errors = form.errors
                error_messages = ['{}: {}'.format(field, ', '.join(messages)) for field, messages in errors.items()]
                error_message = '\n'.join(error_messages)
                final_message = 'El formulario contiene errores. Por favor, corrígelos:\n{} '.format(error_message)
                messages.error(request, final_message)
    else:
        form = CustomUserCreationForm()

    context = {'form': form}
    return render(request, 'Acceso/register.html', context)

def TablaUsuarios(request):
    usuarios_con_grupo = []
    TUsuarios = User.objects.all()

    for usuario in TUsuarios:
        is_authenticated = usuario.is_authenticated
        grupos = usuario.groups.exclude(name='Bloqueado')
        usuarios_con_grupo.append(
            {'usuario': usuario, 'is_authenticated': is_authenticated, 'grupos': grupos})

    return render(request, 'Acceso/user.html', {'usuarios_con_grupo': usuarios_con_grupo})
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------VISTA PRICIPAL HOME O INCIIO-----------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def inicio(request):
    categoria = tblCategoriaGasto.objects.filter(IDAreaTrabajo = 1)
    # Obtener la lista de proyectos con los campos deseados
    proyectos = tblAltaProyecto.objects.filter(IDEstatus_id = 1, IDAreaTrabajo = 1).values("ID", "Folio", "IDEstatus_id__Descripcion",
    "IDCliente_id__Nombre", "Proyecto", "Descripcion", "FechaInicio", "Fechafinal", "Presupuesto")

    fecha_actual = datetime.now().date()
    
    proyectos_con_dias = []  # Lista para almacenar los proyectos con días calculados
   
    for proyecto in proyectos:
        ID_proyecto = proyecto['ID']
        fecha_inicial = proyecto['FechaInicio']
        fecha_final = proyecto['Fechafinal']   
        dias_totales = (fecha_final - fecha_inicial).days
        dias_restantes = (fecha_actual - fecha_inicial).days
        dias_para_porcentaje = (fecha_final - fecha_actual).days
        
        montoXProyecto = tblProyecto.objects.filter(IDProyecto_id=ID_proyecto).values('IDProyecto_id').annotate(total_monto=Sum('Monto'))
        total_monto = montoXProyecto[0]['total_monto'] if montoXProyecto else 0

        porcentaje_acumulado = ((dias_totales - dias_para_porcentaje) / dias_totales) * 100 if dias_totales > 0 else 0
        procentaje = int(porcentaje_acumulado)     
         
        Presupuesto = proyecto['Presupuesto']
        # Asegurarse de trabajar con cadenas antes de usar replace
        if isinstance(Presupuesto, str):
            Presupuesto = Presupuesto.replace(',', '')
        if isinstance(total_monto, str):
            total_monto = total_monto.replace(',', '')

        # Convertir a float
        Presupuesto = float(Presupuesto)
        total_monto = float(total_monto)

        # Realizar los cálculos
        if Presupuesto > 0 and total_monto > 0:
            porcentaje_gastos = ((Presupuesto - total_monto) / Presupuesto) * 100
        else:
            porcentaje_gastos = 100

        # Invertir el porcentaje
        porcentaje2 = 100 - porcentaje_gastos



        
        # Crear un nuevo diccionario con toda la información
        proyecto_info = {
            "ID": proyecto['ID'],
            "Folio": proyecto['Folio'],
            "IDEstatus_id__Descripcion": proyecto['IDEstatus_id__Descripcion'],
            "IDCliente_id__Nombre": proyecto['IDCliente_id__Nombre'],
            "Proyecto": proyecto['Proyecto'],
            "Descripcion": proyecto['Descripcion'],
            "FechaInicio": proyecto['FechaInicio'],
            "Fechafinal": proyecto['Fechafinal'],
            "Presupuesto": proyecto['Presupuesto'],
            "DiasTotales": dias_totales,
            "DiasRestantes": dias_restantes,
            "porcentaje_acumulado": procentaje,
            "porcentaje_gastos": porcentaje2,
            'montoXProyecto': list(montoXProyecto),
            "total_monto": total_monto,  
        }

        # Añadir el diccionario a la lista
        proyectos_con_dias.append(proyecto_info)
        
    fecha_actual = datetime.now().date()
    fecha_formateada = fecha_actual.strftime('%Y-%m-%d') 
    selectPago = tblFormaPago.objects.filter(IDAreaTrabajo = 1)
    selectCategoria = tblCategoriaGasto.objects.filter(IDAreaTrabajo = 1)
    selectProyecto = tblAltaProyecto.objects.filter(IDEstatus_id = 1, IDAreaTrabajo = 1)
    proveedor = tblProyecto.objects.filter(IDAreaTrabajo = 1).values("Proveedor").distinct()    
    return render(request, 'include/index.html', {'categoria': categoria, 'proyectos': proyectos_con_dias, 
    'selectPago':selectPago, 'selectCategoria':selectCategoria, 'fecha_actual':fecha_formateada, 'selectProyecto':selectProyecto, 'proveedor':proveedor})


def mensual(request):
    categoria = tblCategoriaGasto.objects.filter(IDAreaTrabajo = 2)
    # Obtener la lista de proyectos con los campos deseados
    proyectos = tblAltaProyecto.objects.filter(IDEstatus_id = 1, IDAreaTrabajo = 2).values("ID", "Folio", "IDEstatus_id__Descripcion",
    "IDCliente_id__Nombre", "Proyecto", "Descripcion", "FechaInicio", "Fechafinal", "Presupuesto")

    fecha_actual = datetime.now().date()
    
    proyectos_con_dias = []  # Lista para almacenar los proyectos con días calculados

    montoXProyecto = tblProyecto.objects.filter(IDAreaTrabajo = 2).values('IDProyecto_id').annotate(total_monto=Sum('Monto'))
    
    for proyecto in proyectos:
        ID_proyecto = proyecto['ID']
        fecha_inicial = proyecto['FechaInicio']
        fecha_final = proyecto['Fechafinal']   
        dias_totales = (fecha_final - fecha_inicial).days
        dias_restantes = (fecha_actual - fecha_inicial).days
        dias_para_porcentaje = (fecha_final - fecha_actual).days

        porcentaje_acumulado = ((dias_totales - dias_para_porcentaje) / dias_totales) * 100 if dias_totales > 0 else 0
        procentaje = int(porcentaje_acumulado)     
         
        # Obtener el monto total para el proyecto especificado
        montoPorcentajeProyectos = tblProyecto.objects.filter(IDProyecto_id=ID_proyecto).values('IDProyecto_id').annotate(total_monto=Sum('Monto'))
        total_monto = montoPorcentajeProyectos[0]['total_monto'] if montoPorcentajeProyectos else 0
        Presupuesto = proyecto['Presupuesto']
        
        # Asegurarse de trabajar con cadenas antes de usar replace
        if isinstance(Presupuesto, str):
            Presupuesto = Presupuesto.replace(',', '')
        if isinstance(total_monto, str):
            total_monto = total_monto.replace(',', '')

        # Convertir a float
        Presupuesto = float(Presupuesto)
        total_monto = float(total_monto)

        # Realizar los cálculos
        if Presupuesto > 0 and total_monto > 0:
            porcentaje_gastos = ((Presupuesto - total_monto) / Presupuesto) * 100
        else:
            porcentaje_gastos = 100

        # Invertir el porcentaje
        porcentaje2 = 100 - porcentaje_gastos

        
        # Crear un nuevo diccionario con toda la información
        proyecto_info = {
            "ID": proyecto['ID'],
            "Folio": proyecto['Folio'],
            "IDEstatus_id__Descripcion": proyecto['IDEstatus_id__Descripcion'],
            "IDCliente_id__Nombre": proyecto['IDCliente_id__Nombre'],
            "Proyecto": proyecto['Proyecto'],
            "Descripcion": proyecto['Descripcion'],
            "FechaInicio": proyecto['FechaInicio'],
            "Fechafinal": proyecto['Fechafinal'],
            "Presupuesto": proyecto['Presupuesto'],
            "DiasTotales": dias_totales,
            "DiasRestantes": dias_restantes,
            "porcentaje_acumulado": procentaje,
            "porcentaje_gastos": porcentaje2,
            'montoXProyecto': list(montoXProyecto),
            "total_monto": total_monto,  
        }

        # Añadir el diccionario a la lista
        proyectos_con_dias.append(proyecto_info)
        
    fecha_actual = datetime.now().date()
    fecha_formateada = fecha_actual.strftime('%Y-%m-%d') 
    selectPago = tblFormaPago.objects.filter(IDAreaTrabajo = 2)
    selectCategoria = tblCategoriaGasto.objects.filter(IDAreaTrabajo = 2)
    selectProyecto = tblAltaProyecto.objects.filter(IDEstatus_id = 1, IDAreaTrabajo = 2)
    proveedor = tblProyecto.objects.filter(IDAreaTrabajo = 2).values("Proveedor").distinct()    
    return render(request, 'include/gastos.html', {'categoria': categoria, 'proyectos': proyectos_con_dias, 'montoXProyecto':montoXProyecto,
    'selectPago':selectPago, 'selectCategoria':selectCategoria, 'fecha_actual':fecha_formateada, 'selectProyecto':selectProyecto, 'proveedor':proveedor})



