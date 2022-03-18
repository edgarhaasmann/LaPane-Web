from distutils.log import error
from logging import PlaceHolder
from django import forms
from ..userApp.models import Usuarios
from django.contrib.auth.models import User


class AgregarEmpleado(forms.Form):
    nombre = forms.CharField( label='Nombre ',required=True, max_length=30, widget= forms.TextInput(attrs={
        'class':'form-control', 'PlaceHolder':'Nombre', 'autocomplete':'off'}))
    appaterno = forms.CharField(required=True, max_length=30, widget= forms.TextInput(attrs={
        'class':'form-control', 'PlaceHolder':'Apellido paterno', 'autocomplete':'off'}))
    apmaterno = forms.CharField(required=True, max_length=30, widget= forms.TextInput(attrs={
        'class':'form-control', 'PlaceHolder':'Apellido materno', 'autocomplete':'off'}))
    fnaciemiento = forms.DateField(required=True, widget= forms.DateInput(attrs={
        'class':'form-control', 'label':'Fecha Nacimiento', 'type':'date'}))
    user = forms.CharField(required=True, max_length=30, widget= forms.TextInput(attrs={
        'class':'form-control', 'PlaceHolder':'Usuario', 'autocomplete':'off'}))
    password = forms.CharField(required=True, max_length=30, widget= forms.PasswordInput(attrs={
        'class':'form-control', 'PlaceHolder':'Contraseña'}))
    password2 = forms.CharField(label='Repite contraseña',required=True, widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder':'Repita la contraseña'
    }))
    #consulta de usuarios unicos
    def clean_user(self):
        user = self.cleaned_data.get('user')

        if Usuarios.objects.filter(user = user).exists():
            self.add_error('user', 'El usuario ya existe')
            raise forms.ValidationError('El usuario ya existe') 
        return user 
    #confirmacion de contraseña 
    def clean(self):
        cleaned_data = super().clean()

        if cleaned_data.get('password2') != cleaned_data.get('password'):
            self.add_error('password2','La confirmacion de contraseña es erronea')
    
    #guardar los datos         
    def save(self):
        return Usuarios.objects.create_superuser(
            self.cleaned_data.get('nombre'),
            self.cleaned_data.get('appaterno'),
            self.cleaned_data.get('apmaterno'),
            self.cleaned_data.get('fnaciemiento'),
            self.cleaned_data.get('user'),
            self.cleaned_data.get('password')
        )