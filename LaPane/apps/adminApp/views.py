#respuestas
from urllib import response
from django.http import HttpResponse
from django.shortcuts import redirect, render

from LaPane.settings import BASE_DIR
#modelos
from ..userApp.models import Plazas, Usuarios
from ..plazaEmpleadoApp.models import Pedidos, Productos,Ventas, ProductosPlaza
from .models import Empleados, Roles
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
    # try:
    if request.POST['password'] == request.POST['password2']:
        r = Usuarios(nombre=request.POST.get('nombre'), appaterno=request.POST.get('appaterno'),apmaterno = request.POST.get('apmaterno'), fnaciemiento = request.POST.get('fNacimiento'),user= request.POST.get('user'),password= make_password(request.POST.get('password'), None)).save()
        messages.success(request, 'Usuario registrado exitosamente!')
        # print('save!')
    else:
        messages.error(request, 'Las contraseñas no coinciden')
    return redirect('index')
    # except:
    #     messages.error(request, 'Algo ha salido mal y no se pudo registrar el usuario')
    #     return redirect('index')
        # print(''' don't save! ''')
def editUser(request):
    # return render(request,'admin/modalEditUser.html')
    if request.GET.get('id_empleado'):
        data = Usuarios.objects.filter(pk = request.GET.get('id_empleado'))
        dataUser = Empleados.objects.filter(id_usuario = request.GET.get('id_empleado'))
        plz = Plazas.objects.all()
        rol = Roles.objects.all()
        return render(request,'admin/modalEditUser.html',{'data':data,'dataUser':dataUser, 'plz':plz, 'rol':rol})
    else:
        usuario = Empleados.objects.filter(id_usuario = request.GET['empleado'])
        if usuario:
            for u in usuario:
                if not request.GET.get('plaza') and not  request.GET.get('rol'):
                    messages.error(request, 'seleccione la opcion que desee, no se han hecho cambios')
                elif request.GET.get('plaza') or request.GET.get('rol'):
                    if not request.GET.get('plaza'):
                        u.id_rol = Roles.objects.get(pk = request.GET['rol'])    
                        messages.success(request, 'Rol cambiado exitosamente!')
                    elif not request.GET.get('rol'):
                        u.id_plaza = Plazas.objects.get(pk = request.GET['plaza'])
                        messages.success(request, 'Usuario reubicado en la plaza exitosamente!')
                    else:
                        u.id_rol = Roles.objects.get(pk = request.GET['rol'])    
                        u.id_plaza = Plazas.objects.get(pk = request.GET['plaza'])
                        messages.success(request, 'datos cambiados ')
                    
                    u.save()
        else:
            empleados = Empleados()
            empleados.id_usuario = Usuarios.objects.get(pk=request.GET['empleado'])
            empleados.id_plaza = Plazas.objects.get(pk = request.GET['plaza'])
            empleados.id_rol = Roles.objects.get(pk = request.GET['rol'])
            empleados.save()
            messages.success(request, 'El empleado ha sido registrado en la plaza exitosamente!')
    return redirect('index')
def delUser(request):
    r = Usuarios.objects.filter(pk = request.GET['delUser'])
    r.delete()
    messages.success(request, f'El usuario ha sido eliminado exitosamente!')
    return redirect('index')

class Inventario:
    def __init__(self):
        self.productos = Productos()
        self.productosplaza = ProductosPlaza()
        self.plaza = Plazas()

    def getInventio(self, request):
        products = Productos.objects.all()
        return render(request, 'admin/adminInventario.html', {'products':products})
    #metodo para registrar nuevo producto
    def AddProducto(self, request):
        if request.POST.get('nombreProducto') == '' and request.POST.get('cantidad') =='' and request.POST.get('precio') == '':
            messages.warning('Todos los campos deben de estar llenos!')
        else:
            Productos(nombreproducto = request.POST.get('nombreProducto'), cantidad= request.POST.get('cantidad'), precio = request.POST.get('precio')).save()
            messages.success(request, 'Producto registrado')
        return redirect('getProduct')
    #metodo para editar producto
    def editProduct(self, request):
        if request.GET.get('id'):
                p = Productos.objects.filter(pk = request.GET['id'])
                plza = Plazas.objects.all()
                return render(request,'admin/modalEditProduct.html',{'product':p, 'plaza':plza})
        #actualizar datos del producto
        elif request.GET.get('id_producto'):
            producto = Productos.objects.get(pk = request.GET['id_producto'])            
            if request.GET['cantidad']!='':
               producto.cantidad = int(producto.cantidad) + int(request.GET['cantidad'])
               producto.save()
               messages.success(request, 'Cantidad del producto agregada exitosamente')
                    
            elif request.GET['nombreProducto'] or request.GET['precio']:
                if  producto.nombreproducto != request.GET['nombreProducto'] or producto.precio!= float(request.GET['precio']):
                    producto.nombreproducto = request.GET['nombreProducto']
                    producto.precio = request.GET['precio']
                    messages.success(request, 'Producto actualizado exitosamente')
                    producto.save()
                else:
                    messages.warning(request, 'No se recocieron cambios')
            return redirect('getProduct')
        #asignar producto a plaza
        else:
            productoPlaza = ProductosPlaza.objects.filter(id_plaza = request.GET['plaza']).filter(id_producto =request.GET['id_productoAdd'])
            product = Productos.objects.filter(pk = request.GET['id_productoAdd'])
            for p in product:
                p.cantidad = p.cantidad - int(request.GET['cantidad'])
                p.save()
            if productoPlaza:
                for pplz in productoPlaza:
                    pplz.cantidadProductoPlaza = pplz.cantidadProductoPlaza + int(request.GET['cantidad'])
                    pplz.id_producto = Productos.objects.get(pk = request.GET['id_productoAdd'])
                    pplz.id_plaza = Plazas.objects.get(pk = request.GET['plaza'])
                    pplz.save()
                   
                messages.success(request, 'cantidad agregada en la plaza')
            else:
                self.productosplaza.id_producto =  Productos.objects.get(pk = request.GET['id_productoAdd'])
                self.productosplaza.cantidadProductoPlaza =  int(request.GET['cantidad'])
                self.productosplaza.id_plaza = Plazas.objects.get(pk = request.GET['plaza'])
                self.productosplaza.save()
                

                messages.success(request, 'Producto agregado en la plaza')
            return redirect('getProduct')
    #metodo para eliminar producto     
    def delProduct(self, request):
        if request.method =='GET' and request.GET:
            p = Productos.objects.filter(pk = request.GET['delProduct'])
            p.delete()
            messages.success(request, 'Producto eliminado')
            return redirect('getProduct')

def purgVentas(request):
    model = Ventas.objects.all()
    date = datetime.today().strftime('%Y-%m-%d')
    dir = os.path.join(BASE_DIR,'apps/adminApp/ventas')
    try:
        ventas = open(f'{dir}/ventas_de_{date}.doc', 'w')
        ventas.write('''Ventas plaza\n
        \n'

                    ''')
        for i in model:
            if i.id_productoPlaza!=None:
                cantidad = float(i.valortotal)//int(i.id_productoPlaza.id_producto.precio)
                ventas.write(f'''
                ----------------------------------------------------------------
|Nombre del producto: {i.id_productoPlaza.id_producto.nombreproducto} \n| Cantidad producto: {cantidad} \n|Total de venta: $ {i.valortotal} \n| Fecha venta: {i.fventa} \n 
                ----------------------------------------------------------------
                ''')
        ventas.write('''Productos personalizados ( Pedidos )\n
                ''')
        for i in model:
            if i.id_pedido!=None:
                ventas.write(f'''
                ----------------------------------------------------------------
                |Descripcion: {i.id_pedido.descripcionpedido} \n| Cantidad: {(i.id_pedido.cantidadproducto)}\n| Precio: ${i.id_pedido.precio}   \n | Fecha venta: {i.fventa} \n 
                ----------------------------------------------------------------
                ''')
            
        ventas.close()
    except:
        messages.error(request, 'El archivo se en cuentra en uso')
        return redirect('purga')
    raiz = os.path.join(BASE_DIR, 'apps/adminApp/ventas')
    if request.method == 'GET':
        carpeta = []
        with os.scandir(raiz) as directorio:
            for d in directorio:
                carpeta.append(d.name)
        return render(request, 'admin/archivos.html', {'carpeta':carpeta, 'dir': dir})
    else:
        if request.POST.get('archivo'):
            with open('apps/adminApp/ventas/'+request.POST['archivo'],'rb') as dir:
                
                response = HttpResponse(dir)
                response['Content-Disposition'] = "attachment; filename=" + request.POST['archivo']
                Ventas.objects.all().delete()
                Pedidos.objects.all().delete()
                return response
        elif request.POST.get('archivoDel'):
            # os.remove(os.path.basename('apps/adminApp/ventas/{}').format(request.POST['archivoDel']))
            with os.scandir(raiz) as archivoDel:
                for al in archivoDel:
                    if request.POST['archivoDel'] == al.name:
                        os.remove('{}/{}'.format(raiz,al.name))
                        messages.success(request, 'archivo eliminado exitosamente!')
                        return redirect('purga')
        else:
            with os.scandir(raiz) as archivoDel:
                for al in archivoDel:
                    os.remove('{}/{}'.format(raiz,al.name))
            
            messages.success(request, 'Todos los archivos se han eliminado con exito!')
            return redirect('purga')

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


