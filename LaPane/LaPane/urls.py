from django.contrib import admin
from django.urls import path
from apps.userApp import views as authview
from apps.adminApp import views as adminview
urlpatterns = [
    #rutas auth 
    path('', authview.auth, name = 'login'),
    path('logout', authview.out_auth, name = 'logout'),

    #rutas admin 
    path('admin/home', adminview.index, name='index'),
    path('admin/register', adminview.registerUser, name='registerUser'),
    
    #rutas empleadoPlaza
    
    #path('admin/', admin.site.urls),
]
