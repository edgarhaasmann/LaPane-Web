from unicodedata import name
from django.contrib import admin
from django.urls import path
from apps.userApp import views as authview
from apps.adminApp import views as adminview
from apps.plazaEmpleadoApp import views as plazaview
pedidos = plazaview.PedidoAbono()
inventario = adminview.Inventario()
urlpatterns = [
    #rutas auth 
    path('', authview.auth, name = 'login'),
    path('logout', authview.out_auth, name = 'logout'),

    #rutas admin 
    path('admin/home', adminview.index, name='index'),
    path('admin/register', adminview.registerUser, name='registerUser'),
    path('admin/editUser', adminview.editUser, name='editUser'),
    path('admin/delUser', adminview.delUser, name='delUser'),
    
    
    path('admin/adminInventario', inventario.getInventio, name='getProduct'),
    path('admin/registerProduct', inventario.AddProducto, name='registerProduct'),
    path('admin/editProduct',inventario.editProduct, name='editProduct'),
    path('admin/delProduct', inventario.delProduct, name='delProduct'),
    path('admin/estadisticas', adminview.statistics, name='statistics'),
    #rutas empleadoPlaza
    path('ventas/RealizarVenta', plazaview.listProductos, name = 'venta'),
    path('ventas/Venta', plazaview.realizarVenta, name = 'realizarVenta'),
    path('ventas/pedidos', pedidos.pedidosLIst, name='pedidosList'),
    path('ventas/registrarPedido', pedidos.registrarPedido, name='registrarPedido'),
    path('ventas/editPedido', pedidos.editPedido, name='editPedido'),
    path('ventas/delPedido', plazaview.delPedido, name='delPedido'),
    #path('admin/', admin.site.urls),
]
