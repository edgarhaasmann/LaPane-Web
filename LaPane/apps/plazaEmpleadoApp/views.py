
from django.shortcuts import redirect, render
from ..userApp.models import Plazas
from .models import ProductosPlaza, Ventas, Pedidos, Abonos
from django.contrib import messages
from django.views.generic import CreateView
# Create your views here.

def listProductos(request):
    items = ProductosPlaza.objects.filter(id_plaza = 1)
    return render(request,'plazaEmpleado/ventas.html',{'items':items})

def realizarVenta(request):
    for items in request.GET.items():
        print(items)
        print(items)

     
#funcion para abonar a pedido
class PedidoAbono:
    def __init__(self):
        self.pedidos = Pedidos()
        self.abonos = Abonos()
        self.ventas = Ventas()
        self.precio, self.faltante, self.contador = 0,0, 0
    
    def pedidosLIst(self, request):
        pedido = Pedidos.objects.filter(id_plaza=1)
        p = Plazas.objects.filter(pk=1)
        return render(request, 'plazaEmpleado/plazaPedidos.html', {'pedidos':pedido, 'p':p})
    
    #funcion para registrar pedido
    def registrarPedido(self, request):
        if request.method == 'POST':
            pedidos = Pedidos()
            pedidos.id_plaza = Plazas.objects.get(pk = request.POST['id_plaza'])
            pedidos.nombrecliente = request.POST['nombrecliente']
            pedidos.descripcionpedido = request.POST['descripcionpedido']
            price = float(request.POST.get('precio'))
            pedidos.precio = price
            pedidos.cantidadproducto = request.POST['cantidad']
            pedidos.save()
            messages.success(request, 'Pedido registrado!')
        return redirect('pedidosList') 

    def editPedido(self, request):
        if request.GET.get('id_Edit'):
            #datos del pedido
            pedidos = Pedidos.objects.filter(pk=request.GET.get('id_Edit'))
            #cancular abono 
            abonos = Abonos.objects.filter(id_pedido = request.GET.get('id_Edit'))
            self.contador=0
            if abonos:
                for a in abonos:
                    self.contador += a.valorAbono
            for p in pedidos:
                self.precio = p.precio
                self.faltante = p.precio - self.contador
            
            return render(request, 'plazaEmpleado/plazaPedidoAbonar.html', {'items':pedidos, 'total':self.contador, 'faltante':self.faltante})
        else:
            total = self.contador+float(request.GET['montoDelPedido'])
            if float(request.GET.get('montoDelPedido')) > self.precio or total>self.precio:
                messages.error(request, 'El monto supera el precio y por lo tanto no se ha podido realizar el abono')
                return redirect('pedidosList')
            else:
                a = Abonos()
                a.valorAbono = request.GET['montoDelPedido']
                a.id_pedido = Pedidos.objects.get(pk = request.GET.get('id_pedido'))
                messages.success(request, 'El abono se ha hecho exitosamente!')
                a.save()
                
                if total == self.precio:
                    p = Pedidos.objects.get(pk = request.GET.get('id_pedido'))
                    p.estadoPago = 1
                    p.save()

                    self.ventas.valortotal = total
                    self.ventas.id_pedido = Pedidos.objects.get(pk = request.GET.get('id_pedido'))
                    self.ventas.save()
                    messages.success(request, 'El producto se ha vendido!')
                return redirect('pedidosList')
            # Abonos(valorAbono = request.GET.get('montoDelPedido'), id_pedido=request.GET.get('id_pedido'))
#funcion para cancelar pedido
def delPedido(request):
    p = Pedidos.objects.filter(pk = request.GET.get('id_Del'))
    if p:
        p.delete()
    messages.success(request, 'Pedido cancelado exitosamente!')
    return redirect('pedidosList')
         
