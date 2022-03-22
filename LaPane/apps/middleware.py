from django.contrib import messages
from django.forms import ValidationError

from apps.userApp.models import Sessiones
from .adminApp.models import Empleados, Roles
from django.shortcuts import redirect
from datetime import datetime
def notSession(request, val = None):
        messages.error(request, 'No hay session o se ha cerrado ')
        ret = redirect('login')
        ret.delete_cookie('key_rol')
        ret.delete_cookie('key_session')
        return ret


def noModule(request, val=None):
    request.COOKIES['key_session']

def noRol(request, val = None):
    messages.error(request, 'No tiene acceso al modulo')
    ret = redirect('login')
    ret.delete_cookie('key_rol')
    ret.delete_cookie('key_session')
    return ret, val



    


