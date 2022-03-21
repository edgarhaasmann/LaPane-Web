from random import choice
from django.shortcuts import redirect, render
from .models import Usuarios, Sessiones
from ..adminApp.models import Empleados 
from django.contrib.auth import authenticate , login, logout
from django.contrib.auth.hashers import check_password, make_password
from django.contrib import messages
from django.template.loader import render_to_string
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
print(session())
def auth(request): 
    date = datetime.now()
    expiracion = date+ timedelta(days=1)
    print(date, expiracion)
    if request.method == 'GET':
        return render(request,'index.html')
    elif request.method =='POST':
        userName= request.POST['user']
        password = request.POST['password'] 
        try:
            isUser = Usuarios.objects.get(user = userName)
            hisPassword = handler.verify(password, isUser.password)
            if isUser and hisPassword == True :
                    try:
                        key_session = session()
                        isEmpleado=Empleados.objects.get(id_usuario = isUser.id_usuario)
                        if isEmpleado and isEmpleado.id_rol.tipoRol=='admin':
                            ret = redirect('index')
                            ret.set_cookie('key_session', key_session, expires=60)
                            Sessiones(id_usuario = Usuarios.objects.get(id_usuario = isEmpleado.id_usuario.id_usuario ), key_session = key_session, key_expire = expiracion).save()
                            return ret
                        elif isEmpleado and isEmpleado.id_rol.tipoRol == 'empleado':
                            ret = redirect('venta')
                            ret.set_cookie('key_session', key_session, expires=60)
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
def out_auth(request):
    logout(request)#funcion para cerrar la sesion 
    messages.success(request, 'sesion cerrada')
    return redirect('login')

