from telnetlib import AUTHENTICATION
from urllib import request
from django.shortcuts import redirect, render
from .models import Usuarios
from django.contrib.auth import authenticate , login, logout
from django.contrib import messages
# Create your views here.


def auth(request):
    if request.method =='POST':
        user = request.POST.get('user')
        password = request.POST.get('password')
        if user == ' ' or password == ' ':
            messages.warning(request, 'Los campos no pueden estar vacios')
        else:
            user = authenticate(user = user, password= password)
            if user:
                login(request, user)# genera la sesion 
                messages.success(f'Bienvenido, {user.user}')
                return 
            else:
                messages.error(request, ' El usuario y/o contraseña son incorrectos')

    return render(request ,'index.html')

def out_auth(request):
    logout(request)#funcion para cerrar la sesion 
    messages.success(request, 'sesion cerrada')
    return redirect('login')