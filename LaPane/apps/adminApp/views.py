from django.shortcuts import redirect, render
from ..userApp.models import Plazas, Usuarios
from ..plazaEmpleadoApp.models import Productos
from django.contrib.auth.hashers import make_password, check_password
from django.views.generic import ListView, CreateView

#libreria para los mensajes 
from django.contrib import messages

from datetime import datetime
# Create your views here.
def index(request):

    user = Usuarios.objects.all()
    return render(request, 'admin/agregar.html', {'data':user})

def registerUser(request):
    date= datetime.now()
    print(date)
    try:
        r = Usuarios(nombre=request.POST.get('nombre'), appaterno=request.POST.get('appaterno'),apmaterno = request.POST.get('apmaterno'), fnaciemiento = request.POST.get('fNacimiento'),user= request.POST.get('user'),password= make_password(request.POST.get('password'))).save()
        messages.success(request, 'Usuario registrado exitosamente!')
        # print('save!')
        return redirect('index')
    except:
        messages.error(request, 'Algo ha salido mal y no se pudo registrar el usuario')
        return redirect('index')
        # print(''' don't save! ''')
def delUser(request):
    r = Usuarios.objects.filter(pk = request.GET['delUser'])
    #r.delete()
    messages.success(request, f'El usuario ha sido eliminado exitosamente!')
    return redirect('index')

def getInventio(request):
    products = Productos.objects.all()
    return render(request, 'admin/adminInventario.html', {'products':products})

def AddProducto(request):
    if request.POST.get('nombreProducto') == '' and request.POST.get('cantidad') =='' and request.POST.get('precio') == '':
      messages.warning('Todos los campos deben de estar llenos!')
      return redirect('getProduct')
    else:
        Productos(nombreproducto = request.POST.get('nombreProducto'), cantidad= request.POST.get('cantidad'), precio = request.POST.get('precio')).save()
        messages.success(request, 'Producto registrado')
        return redirect('getProduct')
    
def editProduct(request):
    if request.GET.get('id'):
        p = Productos.objects.filter(pk = request.GET['id'])
        plza = Plazas.objects.all()
        return render(request,'admin/modalEditProduct.html',{'product':p, 'plaza':plza})

    else: 
        p = Productos.objects.get(pk = request.GET.get('id_producto'))
        print(type(p.cantidad), type(request.GET.get('cantidad')))
        if p.nombreproducto != request.GET.get('nombreProducto') or p.precio != float(request.GET.get('precio')):
            p.nombreproducto = request.GET['nombreProducto']
            p.precio = request.GET['precio']
            p.save()
            messages.success(request, 'Producto actualizado')
            return redirect('getProduct')
        else:
            messages.error(request,'No se reconocieron cambios')
            return redirect('getProduct')
def delProduct(request):
    if request.method =='GET' and request.GET:
        p = Productos.objects.filter(pk = request.GET['delProduct'])
        p.delete()
        messages.success(request, 'Producto eliminado')
        return redirect('getProduct')