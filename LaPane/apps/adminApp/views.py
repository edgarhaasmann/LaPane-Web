from django.shortcuts import redirect, render
from ..userApp.models import Usuarios
# Create your views here.
def index(request):

    data = Usuarios.objects.all()
    return render(request, 'admin/agregar.html', {'data': data})

def registerUser(request):
    
    return redirect('index')
