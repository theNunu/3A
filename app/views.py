from django.shortcuts import render
from django.http import HttpResponse
from .forms import newCreateClientForm
#inicio
def home (request):
    return render(request,'Home.html')

#Pages
def clientes (request):
    return render(request,'pages/clientes.html')

def sucursales (request):
    return render(request,'pages/sucursales.html')

def ti (request):
    return render(request,'pages/ti.html')
