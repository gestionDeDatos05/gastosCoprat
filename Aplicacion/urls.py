from django.urls import path
from . import views
from Aplicacion.Consultas.Catalogos import agregarC, editarC, mostrarC, actualizarC
from Aplicacion.Consultas.Procesos import agregarP, editarP, mostrarP, actualizarP
from Aplicacion.Consultas.Subtablas import agregarS, editarS, mostrarS, actualizarS
from Aplicacion.Consultas.Reportes import mostrarR
from Aplicacion.Consultas.Usuarios import mostrarU
from django.contrib.auth.views import LoginView, LogoutView
from .views import CustomLoginView
urlpatterns = [
     #  Presentacion
    # USUARIOS LOGIN, REGISTER O LOGOUT
    path('Logout/', LogoutView.as_view(template_name='Acceso/logout.html'), name='Logout'),
    path('Login/', CustomLoginView.as_view(), name='Login'),
    path('Register/', views.Register, name='Register'),
    path('Asignar_permisos/', mostrarU.asignarUsuario, name='A_Permisos'),
    path('Usuario/', views.TablaUsuarios, name='T_Usuario'),
     
    path('', views.inicio, name='T_Inicio'),
    path('GASTOS_MENSUALES/', views.mensual, name='Mensual'),
    
    # VISTA PARA MOSTRAR LAS TABLAS DE LOS REGISTROS DADOS DE ALTA
    path('Clientes_Proyecto/', mostrarC.tablaCliente, name='T_Clientes'),
    path('Clientes_Mensuales/', mostrarC.tablaClienteMensuales, name='TM_Clientes'),
    
    path('Forma_de_pago_Proyecto/', mostrarC.tablaFormaDePago, name='T_Forma_de_pago'),
    path('Forma_de_pago_Mensuales/', mostrarC.tablaFormaDePagoMensuales, name='TM_Forma_de_pago'),
    
    path('Catalogo_Proyecto/', mostrarC.tablaCategoria, name='T_Categoria'),
    path('Catalogo_Mensuales/', mostrarC.tablaCategoriaMensuales, name='TM_Categoria'),
    
    path('Proyecto/', mostrarC.tablaProyecto, name='T_Proyecto'),
    path('Mensualidad/', mostrarC.tablaProyectoMensuales, name='T_Mensual'),
    



    # VISTA PARA EDITAR LOS REGISTROS DADOS DE ALTA
    path('Editar_Clientes/', editarC.editarCliente, name='E_Clientes'),
    path('Editar_Forma_de_pago/', editarC.editarFormaDePago, name='E_Forma_de_pago'),
    path('Editar_Catalogo/', editarC.editarCategoria, name='E_Categoria'),
    path('Editar_Proyecto/', editarC.editarAltaProyecto, name='E_Proyecto'),
    
    # VISTA PARA ACTUALIZAR LOS REGISTROS DADOS DE ALTA
    path('Actualizar_Clientes/', actualizarC.actualizarCliente, name='A_Clientes'),
    path('Actualizar_Forma_de_pago/', actualizarC.actualizarFormaDePago, name='A_Forma_de_pago'),
    path('Actualizar_Categoria/', actualizarC.actualizarCategoria, name='A_Categoria'),
    path('Actualizar_Proyecto/', actualizarC.actualizarAltaProyecto, name='A_Proyecto'),
    path('Actualizar_Estatus_Proyecto/', actualizarC.actualizarEstatusProyecto, name='AE_Proyecto'),
    
    # APARTADO PARA GUARDAR LOS  REGISTROS Y DARLOS DE ALTA
    path('Guardar_Clientes/', agregarC.guardarCliente, name='G_Clientes'),
    path('Guardar_Forma_De_Pago/', agregarC.guardarFormaDePago, name='G_FormaDePago'),
    path('Guardar_Categoria/', agregarC.guardarCategoria, name='G_Categoria'),
    path('Guardar_Proyecto/', agregarC.guardarProyecto, name='G_Proyecto'),
    

    # DETALLADO DE GASTOS POR PROYECTOS
    path('Detallado_De_Gastos_Por_Proyecto/', mostrarP.detalleProyecto, name='D_Proyecto'),
    path('Detallado_De_Gastos_Por_Mensualidad/', mostrarP.detalleGastos, name='D_Gastos'),
    # VISTA PARA EDITAR LOS REGISTROS DADOS DE ALTA
    path('Editar_Detallado_De_Gastos_Por_Proyecto/', editarP.editarProyecto, name='ED_Proyecto'),
    # VISTA PARA EDITAR LOS REGISTROS DADOS DE ALTA
    path('Cancelar_Detallado_De_Gastos_Por_Proyecto/', editarP.cancelarEditadoProyecto, name='CD_Proyecto'),
    path('Cancelar_Detallado_De_Gastos_Por_Mensualidad/', editarP.cancelarEditadoMensuales, name='CD_Mensuales'),
    # VISTA PARA ACTUALIZAR LOS REGISTROS DADOS DE ALTA
    path('Actualizar_Detallado_De_Gastos_Por_Proyecto/', actualizarP.actualizarProyecto, name='AD_Proyecto'),
    # GUARDAR DETALLADO DE GASTOS POR PROYECTOS
    path('Guardar_Detallado_De_Gastos_Por_Proyecto/', agregarP.guardarDetalleProyecto, name='GD_Proyecto'),


    # DETALLADO DE GASTOS POR PROYECTOS
    path('Estatus/', mostrarS.tablaEstatus, name='T_Estatus'),
    # VISTA PARA EDITAR LOS REGISTROS DADOS DE ALTA
    path('Editar_Estatus/', editarS.editarEstatus, name='E_Estatus'),
    # VISTA PARA ACTUALIZAR LOS REGISTROS DADOS DE ALTA
    path('Actualizar_Estatus/', actualizarS.actualizarEstatus, name='A_Estatus'),
    # GUARDAR DETALLADO DE GASTOS POR PROYECTOS
    path('Guardar_Estatus/', agregarS.guardarEstatus, name='G_Estatus'),
    
    # REPORTE GASTOS POR PROYECTOS
    path('Reporte_gastos_proyecto/', mostrarR.reportesProyecto, name='R_Proyecto'),
    path('Reporte_gastos_mensuales/', mostrarR.reportesMensuales, name='R_Mensuales'),
]