from django.shortcuts import redirect, render
from .models import Usuarios
from ..adminApp.models import Empleados 
from django.contrib.auth import authenticate , login, logout
from django.contrib.auth.hashers import check_password, make_password
from django.contrib import messages
from passlib.hash import django_pbkdf2_sha256 as handler
def auth(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    elif request.method =='POST':
        userName= request.POST['user']
        password = request.POST['password'] 
        try:
            isUser = Usuarios.objects.get(user = userName)
            if isUser :
                print('1')
                hisPassword = handler.verify(password, isUser.password)
                print(hisPassword)
                if hisPassword == True:
                    print('2')
                    isEmpleado=Empleados.objects.get(id_usuario = isUser.id_usuario)
                    if isEmpleado and isEmpleado.id_rol.tipoRol=='admin':
                        print('3')
                        return redirect('index')
                    elif isEmpleado and isEmpleado.id_rol.tipoRol == 'empleado':
                        print('4')
                        return redirect('venta')
                    if not isEmpleado:
                        print('5')
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