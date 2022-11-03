from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.template import RequestContext


@login_required

def index(request):
    return render(request, 'index.html')

def servicio(request):
    return render(request, 'servicio.html')

def inicio(request):
    return render(request, 'inicio.html')

def galeria(request):
    return render(request, 'galeria.html')
    
def somos(request):
    return render(request, 'somos.html')

def login(request):
    return render(request, 'login.html')

def registro(request):
    return render(request, 'registration/registro.html')

def formulario(request):
    return render(request, 'formulario.html')




