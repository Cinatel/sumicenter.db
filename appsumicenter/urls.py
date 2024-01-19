from django.urls import path
from . import views


urlpatterns = [

    #REGISTRO DE USUARIO
    path('', views.registro, name="registro"),
    path('registrar/', views.registrar, name="registrar"),
    

    # LOGIN DE USUARIO
    path('Ingresar/', views.inicioSesion, name="LogueoUsuario"),
    path('login/', views.logueo, name="login"),
    path('logout/', views.deslogeo, name="logout"),

    #PLANTILLAS
    path('truper/', views.Truper, name="truper"),
    path('inicio/', views.inicio, name="inicio"),

    #REGISTRO DE ITEMS
    path('registroTruper/', views.registroTruper, name="registroTruper"),
    path('registroSumicenter/', views.registroSumicenter, name="registroSumicenter"),

    #FUNCIONES PARA ELIMIANR PRODUCTOS
    path('borrarTruper/<int:id>', views.eliminarTruper, name="eliminarTruper"),
    path('borrarProducto/<int:id>', views.eliminarProducto, name="eliminarProducto"),   

    #FUNCIONES PARA EDITAR PRODUCTOS
    path('editarProducto/<int:id>', views.editarProducto, name="editarProducto"),
    path('actualizarProducto/', views.actualizarProducto, name="actualizarProducto"),

    path('editarTruper/<int:id>', views.editarTruper, name="editarTruper"),
    path('actualizarTruper/', views.actualizarTruper, name="actualizarTruper"),

    
]
