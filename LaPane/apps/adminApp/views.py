#respuestas
from django.shortcuts import redirect, render

from LaPane.settings import BASE_DIR
#modelos
from ..userApp.models import Plazas, Usuarios
from ..plazaEmpleadoApp.models import Productos,Ventas, ProductosPlaza
from .models import Empleados
#encryptacion de contraseñas 
from django.contrib.auth.hashers import make_password, check_password
from django.views.generic import ListView, CreateView
#libreria para los mensajes 
from django.contrib import messages

from datetime import datetime
import os

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
def editUser(request):
    # return render(request,'admin/modalEditUser.html')
    if request.GET.get('id_empleado'):
        data = Usuarios.objects.filter(pk = request.GET.get('id_empleado'))
        plz = Plazas.objects.all()
        return render(request,'admin/modalEditUser.html',{'data':data, 'plz':plz})
    else:
        empleados = Empleados()
        empleados.id_usuario = Usuarios.objects.get(pk=request.GET['empleado'])
        empleados.id_plaza = Plazas.objects.get(pk = request.GET['plaza'])
        empleados.save()
        messages.success(request, 'El empleado ha sido registrado en la plaza exitosamente!')
    return redirect('index')
def delUser(request):
    r = Usuarios.objects.filter(pk = request.GET['delUser'])
    r.delete()
    messages.success(request, f'El usuario ha sido eliminado exitosamente!')
    return redirect('index')

def getInventio(request):
    products = Productos.objects.all()
    return render(request, 'admin/adminInventario.html', {'products':products})

def AddProducto(request):
    if request.POST.get('nombreProducto') == '' and request.POST.get('cantidad') =='' and request.POST.get('precio') == '':
      messages.warning('Todos los campos deben de estar llenos!')
    else:
        Productos(nombreproducto = request.POST.get('nombreProducto'), cantidad= request.POST.get('cantidad'), precio = request.POST.get('precio')).save()
        messages.success(request, 'Producto registrado')
    return redirect('getProduct')
    
def editProduct(request):
    if request.GET.get('id'):
        p = Productos.objects.filter(pk = request.GET['id'])
        plza = Plazas.objects.all()
        return render(request,'admin/modalEditProduct.html',{'product':p, 'plaza':plza})
    elif request.GET.get('plaza'):
        producto = Productos.objects.filter(pk = request.GET['id_producto'])
        for p in producto:
            if p.cantidad <  int(request.GET['cantidad']):
                messages.error(request, 'La cantidad supera las existencias')
            else: 
                productoPlaza = ProductosPlaza.objects.filter(id_producto = request.GET['id_producto'] )
                if productoPlaza:
                    for pplz in productoPlaza:
                        pplz.cantidadProductoPlaza = pplz.cantidadProductoPlaza + int(request.GET['cantidad'])
                        pplz.save()
                    for p in producto:
                            p.cantidad = p.cantidad - int(request.GET['cantidad'])
                            p.save()
                else:
                    pPlaza = ProductosPlaza()
                    pPlaza.cantidadProductoPlaza = request.GET['cantidad']
                    pPlaza.id_producto = Productos.objects.get(pk = request.GET['id_producto'])
                    pPlaza.id_plaza = Plazas.objects.get(pk = request.GET['plaza'])
                    pPlaza.save()
                    for p in producto:
                        p.cantidad = p.cantidad - int(request.GET['cantidad'])
                        p.save()
                messages.success(request, 'Producto registrado en la plaza')
    else: 
        p = Productos.objects.get(pk = request.GET.get('id_producto'))
        print(type(p.cantidad), type(request.GET.get('cantidad')))
        if p.nombreproducto != request.GET.get('nombreProducto') or p.precio != float(request.GET.get('precio')) or p.cantidad!= int(request.GET['cantidad']):
            p.nombreproducto = request.GET['nombreProducto']
            p.cantidad = p.cantidad + int(request.GET['cantidad'])
            p.precio = request.GET['precio']
            p.save()
            messages.success(request, 'Producto actualizado')
        else:
            messages.error(request,'No se reconocieron cambios')
    return redirect('getProduct')
def delProduct(request):
    if request.method =='GET' and request.GET:
        p = Productos.objects.filter(pk = request.GET['delProduct'])
        p.delete()
        messages.success(request, 'Producto eliminado')
        return redirect('getProduct')

def purgVentas(t):
    model = Ventas.objects.all()
    date = datetime.today().strftime('%Y-%m-%d')
    dir = os.path.join(BASE_DIR,'apps/adminApp/ventas')
    ventas = open(f'{dir}/ventas_de_{date}.txt', 'w')
    ventas.write('          Nombre del producto| Total | fecha de venta ')
    for i in model:
        ventas.write(f'''
        ----------------------------------------------------------------
        |{i.id_productoPlaza.id_producto.nombreproducto} | {i.valortotal}    |{i.fventa} \n 
        ----------------------------------------------------------------
        ''')
    ventas.close()

def statistics(request):

    data = Ventas.objects.all()
    productos,votos = [],[]
    for d in data:
        if d.id_productoPlaza!=None:
            if d.id_productoPlaza.id_producto.nombreproducto not in productos:
                productos.append(d.id_productoPlaza.id_producto.nombreproducto)
                precio, total = float(d.id_productoPlaza.id_producto.precio),float(d.valortotal)
                votos.append(total//precio)
            else:
                for p in range(len(productos)):
                    if productos[p] == d.id_productoPlaza.id_producto.nombreproducto:
                        precio, total = float(d.id_productoPlaza.id_producto.precio),float(d.valortotal)
                        votos[p] = votos[p] +(total//precio)
                        
        if d.id_pedido!=None:
            if 'productos personalizados' not in productos:
                productos.insert(0,'productos personalizados')
                votos.insert(0, d.id_pedido.cantidadproducto)
            else:
                votos[0] = int(votos[0] + int(d.id_pedido.cantidadproducto))
    return render(request, 'admin/statistics.html',{'nombres':productos, 'votos':votos})


