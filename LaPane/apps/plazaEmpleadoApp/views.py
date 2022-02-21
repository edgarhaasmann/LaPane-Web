from itertools import product
from django.shortcuts import redirect, render
from .models import Productos, Ventas
# Create your views here.

def listProductos(request):
    items = Productos.objects.filter(id_plaza = 1)
    return render(request,'plazaEmpleado/ventas.html',{'items':items})

def realizarVenta(request):
    newProducto = request.POST.keys()
    print(newProducto)
    # productoVenta = Productos.objects.get(nombreproducto = request.POST.get('nombreProducto'))
    # productoVenta.cantidad = int(request.POST.get('cantidad'))
    # productoVenta.save() 
    return redirect('venta')