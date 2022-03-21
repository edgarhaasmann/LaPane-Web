from django.contrib import messages
from .adminApp.models import Empleados, Roles
from django.shortcuts import redirect
def notSession(request, val = None):
    if val == None:
        messages.error(request, 'No hay session o se ha cerrado ')
        return redirect('login')
    else:
        return None

def noModule(request, val=None):
    Empleados

def noRol(request, val = None):
    pass

def noPlaza(request, val=None):
    pass

def timeExpire(request, val=None):
    pass
