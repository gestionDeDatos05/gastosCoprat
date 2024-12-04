from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect

def asignarUsuario(request):
    IDUsuario = request.POST['id_usuario']
    usuario = User.objects.get(id=IDUsuario)

    # Obtener el nuevo grupo
    IDEmpleado = 2
    nuevo_grupo = Group.objects.get(id=IDEmpleado)

    # Eliminar todos los grupos anteriores del usuario
    usuario.groups.clear()

    # Asignar el nuevo grupo al usuario
    usuario.groups.add(nuevo_grupo)

    # Guardar los cambios
    usuario.save()

    return redirect('T_Usuario')
