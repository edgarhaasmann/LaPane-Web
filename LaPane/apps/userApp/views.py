from urllib import request
from django.shortcuts import redirect, render
from .models import Usuarios
from django.contrib.auth import authenticate , login, logout
from django.contrib.auth.hashers import check_password
from django.contrib import messages
# Create your views here.


def auth(request):
    if request.POST.get('user') and request.POST.get('password'):
        username = request.POST['user']
        password = request.POST['password']

        user = authenticate(user = username, password = password)
        if user:
            print('sussfuly')
    else:
        redirect('login')

    # if request.POST.get('user') and request.POST.get('password'):
    #     u = request.POST['user']
    #     p = request.POST['password']
    #     usuario = Usuarios.objects.get(user = u)
        
    #     # check_password('12345', usuario.password)
    #     print(check_password('12345', usuario.password))
    #     messages.success(request, 'datos resividos')

    # else:
    #     messages.error(request, 'Los campos tienen que estar llenos')


    # print(request.POST['user'])
    # print(request.POST['password'])
    
    # u = Usuarios.objects.get(user = request.POST.get('user'))
    # print(u)
    # if request.method =='POST':
    #     user = request.POST.get('user')
    #     password = request.POST.get('password')

    #     try:
    #         autenticacion = Usuarios.objects.get(user = user)
    #         check_password(password)
    #         if autenticacion:
    #             print('ok')
    #     except:
    #         print('Error!')  
    # # if request.method =='POST':
    # #     user = request.POST.get('user')
    # #     password = request.POST.get('password')
    # #     print(user, password)
    # #     if user == ' ' or password == ' ':
    # #         messages.warning(request, 'Los campos no pueden estar vacios')
    # #     else:
    # #         user = authenticate(user = user, password= password)
    # #         if user:
    # #             login(request, user)# genera la sesion 
    # #             messages.success(f'Bienvenido, {user.user}')
    # #             return 
    # #         else:
    # #             messages.error(request, ' El usuario y/o contraseña son incorrectos')

    return render(request ,'index.html')

def out_auth(request):
    logout(request)#funcion para cerrar la sesion 
    messages.success(request, 'sesion cerrada')
    return redirect('login')
