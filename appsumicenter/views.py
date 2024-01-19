from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login , logout, hashers
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.db.models import Q
from .models import productos, truper
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
# Create your views here.

@login_required
def inicio(request):
    busqueda = request.GET.get("busqueda")
    producto = productos.objects.all()
    trupe = truper.objects.all()
    if busqueda:
        producto = productos.objects.filter(
            Q(serial__icontains = busqueda) |
            Q(codigo__icontains = busqueda) |
            Q(EAN__icontains = busqueda) |
            Q(modelo__icontains = busqueda)
            ).distinct()
        trupe = truper.objects.filter(
            Q(serial__icontains = busqueda) |
            Q(codigo__icontains = busqueda) |
            Q(EAN__icontains = busqueda) |
            Q(modelo__icontains = busqueda)
            ).distinct()
    context = {'producto': producto, 'truper': trupe}
    return render(request, 'index.html', context)

def inicioSesion(request):
    return render(request, 'login.html')

def registro(request):
    return render(request, 'register.html')

def registrar(request):
    username = request.POST['user']
    first_name = request.POST ['first_name']
    last_name = request.POST['last_name']
    password = request.POST['password']
    email = request.POST['email']

    if condiciones(email):
        usuario = User()
        usuario.username = username
        usuario.first_name = first_name
        usuario.last_name = last_name
        usuario.password =hashers.make_password(password, salt=None, hasher='default')
        usuario.email = email
        usuario.save()

        return redirect('LogueoUsuario')
    else:
        return render(request, 'error/registrationError.html')

def condiciones(email):
    if email == "laineza420@gmail.com":
        return True
    else:
        return False


def logueo(request):
    usuario = request.POST['user']
    contraseña = request.POST['password']

    user = authenticate(request, username = usuario , password = contraseña)
    if user is not None:
        login(request, user)
        return redirect('inicio')
    else:
        return render(request, "error/loginError.html")
    
def deslogeo(request):
    logout(request)
    return redirect("LogueoUsuario")

#PLANTILLAS DE BASE DE DATOS"

def Truper(request):
    busqueda = request.GET.get("busqueda")
    producto = productos.objects.all()
    trupe = truper.objects.all()
    if busqueda:
        producto = productos.objects.filter(
            Q(serial__icontains = busqueda) |
            Q(codigo__icontains = busqueda) |
            Q(EAN__icontains = busqueda) |
            Q(modelo__icontains = busqueda)
            ).distinct()
    
    if busqueda:
        trupe = truper.objects.filter(
            Q(serial__icontains = busqueda) |
            Q(codigo__icontains = busqueda) |
            Q(EAN__icontains = busqueda) |
            Q(modelo__icontains = busqueda)
            ).distinct()
    context = {'truper': trupe, 'producto': producto}
    return render(request, 'tablas/truper.html', context)



#FUNCIONES PARA REGISTRO DE PRODUCTOS
def registroTruper(request):
    modelo = request.POST['modelo']
    serial = request.POST['serial']
    descripcion = request.POST['codigo']
    fecha_ingreso = request.POST['fecha-ingreso']
    precio = request.POST['EAN']
    orden = request.POST['orden']
    factura = request.POST['factura']
    cantidad = request.POST['cantidad']
 

    registro = truper()
    registro.modelo = modelo
    registro.serial = serial
    registro.codigo = descripcion
    registro.fecha = fecha_ingreso
    registro.EAN = precio
    registro.orden = orden
    registro.factura = factura
    registro.cantidad = cantidad

    registro.save()

    return redirect('truper')


def registroSumicenter(request):
    modelo = request.POST['modelo']
    serial = request.POST['serial']
    descripcion = request.POST['codigo']
    fecha_ingreso = request.POST['fecha-ingreso']
    precio = request.POST['EAN']
    orden = request.POST['orden']
    factura = request.POST['factura']
    cantidad = request.POST['cantidad']

    registro = productos()
    registro.modelo = modelo
    registro.serial = serial
    registro.codigo = descripcion
    registro.fecha = fecha_ingreso
    registro.EAN = precio
    registro.orden = orden
    registro.factura = factura
    registro.cantidad = cantidad

    registro.save()

    return redirect('inicio')



#FUNCIONES PARA ELIMINAR PRODUCTOS
def eliminarTruper(request, id):
    trupe = truper.objects.get(pk=id)
    trupe.delete()
    return redirect('truper')

def eliminarProducto(request, id):
    producto = productos.objects.get(pk=id)
    producto.delete()
    return redirect('inicio')



#FUCIONES PARA EDITAR ELEMENTOS
def editarTruper(request, id):
    producto = truper.objects.get(pk=id)
    context = {'producto': producto}
    return render(request, 'editar/editarTruper.html', context)

def actualizarTruper(request):
    id = request.POST['id']
    modelo = request.POST['modelo']
    serial = request.POST['serial']
    descripcion = request.POST['codigo']
    fecha = request.POST['fecha']
    precio = request.POST['EAN']
    orden = request.POST['orden']
    factura = request.POST['factura']
    cantidad = request.POST['cantidad']

    item = truper()
    item.id = id
    item.modelo = modelo
    item.serial = serial
    item.codigo = descripcion
    item.fecha = fecha
    item.EAN = precio
    item.orden = orden
    item.factura = factura
    item.cantidad = cantidad

    item.save()
    return redirect('truper')

def editarProducto(request, id):
    producto = productos.objects.get(pk=id)
    context = {'producto': producto}
    return render(request, 'editar/editarProducto.html', context)

def actualizarProducto(request):
    id = request.POST['id']
    modelo = request.POST['modelo']
    serial = request.POST['serial']
    descripcion = request.POST['codigo']
    fecha = request.POST['fecha']
    precio = request.POST['EAN']
    orden = request.POST['orden']
    factura = request.POST['factura']
    cantidad = request.POST['cantidad']

    item = productos()
    item.id = id
    item.modelo = modelo
    item.serial = serial
    item.codigo = descripcion
    item.fecha = fecha
    item.EAN = precio
    item.orden = orden
    item.factura = factura
    item.cantidad = cantidad

    item.save()
    return redirect('inicio')

