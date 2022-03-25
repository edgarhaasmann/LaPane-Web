from random import choice
from django.shortcuts import redirect, render
from .models import Usuarios, Sessiones
from ..adminApp.models import Empleados 
from django.contrib.auth.hashers import check_password, make_password
from django.contrib import messages
from datetime import datetime, timedelta
from passlib.hash import django_pbkdf2_sha256 as handler
def session():
    valores = ['e','i','1','2','o','u','¿','3','4','+','5','6','7','8','9','a']
    llaveGenerada = ''
    for i in range(20):
            llaveGenerada += (choice(valores))
            if len(llaveGenerada) == 4 or len(llaveGenerada) == 9 or len(llaveGenerada) == 14 or len(llaveGenerada) == 19 :
                llaveGenerada +='$'
    return llaveGenerada
def auth(request): 
    date = datetime.now().date()

    expireDateDB = Sessiones.objects.filter(key_expire = date).delete()

    expiracion = date+ timedelta(days=1)
    if request.method == 'GET':
        return render(request,'index.html')
    elif request.method =='POST':
        userName= request.POST['username']
        password = request.POST['password'] 
        try:
            isUser = Usuarios.objects.get(user = userName)
            hisPassword = handler.verify(password, isUser.password)
            if isUser.user == userName and hisPassword == True :
                    try:
                        key_session = session()
                        isEmpleado=Empleados.objects.get(id_usuario = isUser.id_usuario)
                        if isEmpleado and isEmpleado.id_rol.tipoRol=='admin':
                            ret = redirect('index')
                            ret.set_cookie('key_session', key_session, expires=43200)
                            ret.set_cookie('key_rol', '4<$4dM1n', expires=43200)
                            Sessiones(id_usuario = Usuarios.objects.get(id_usuario = isEmpleado.id_usuario.id_usuario ), key_session = key_session, key_expire = expiracion).save()
                            return ret
                        elif isEmpleado and isEmpleado.id_rol.tipoRol == 'empleado':
                            ret = redirect('venta')
                            ret.set_cookie('key_session', key_session, expires=43200)
                            ret.set_cookie('key_rol', '#mpl$3Ad0', expires=43200)
                            Sessiones(id_usuario = Usuarios.objects.get(id_usuario = isEmpleado.id_usuario.id_usuario ), key_session = key_session, key_expire = expiracion).save()
                            return ret

                    except:
                        messages.error(request, 'Aun no tienes rol contacta al administrador')
                        return redirect('login')  
            else:
                messages.error(request, 'Usuario y/o contraseña incorrectos')
                return redirect('login') 
        except BaseException:
            messages.error(request, 'Usuario y/o contraseña incorrectos')
            return redirect('login')
#funcion para cerrar la sesion     
def out_auth(request):
    Sessiones.objects.get(key_session = request.COOKIES['key_session']).delete()
    ret = redirect('login')
    ret.delete_cookie('key_session')
    ret.delete_cookie('key_rol')
    messages.success(request, 'sesión cerrada')
    return ret

