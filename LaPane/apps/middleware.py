from django.contrib import messages
from django.forms import ValidationError

from apps.userApp.models import Sessiones
from .adminApp.models import Empleados, Roles
from django.shortcuts import redirect
from datetime import datetime
def notSession(request, val = None):
        # Sessiones.objects.get(key_session = request.COOKIES['key_session']).delete()
        messages.error(request, 'No hay sesión iniciada o se ha cerrado ')
        ret = redirect('login')
        ret.delete_cookie('key_rol')
        ret.delete_cookie('key_session')
        return ret


def noModule(request, val=None):
    request.COOKIES['key_session']

def noRol(request, val = None):
    try:
        Sessiones.objects.get(key_session = request.COOKIES['key_session']).delete()
        messages.error(request, 'No tiene acceso al modulo')
        ret = redirect('login')
        ret.delete_cookie('key_rol')
        ret.delete_cookie('key_session')
        return ret
    except:
        return notSession(request)


    


