from django.shortcuts import render
from django.http import HttpResponse
from .forms import newCreateClientForm

# Create your views here.
def first (request):
    return render(request, 'Home.html')

#===========================
def Cliente(request):
    return render(request,'Cliente.html')

def Comentario(request):
    return render(request, 'Comentario.html')

def DetalleCliente(request):
    return render(request, 'DetalleCliente.html')

def Empleado(request):
    return render(request, 'Empleado.html')

def Entrenador(request):
    return render(request, 'Entrenador.html')

def EquipoEntrenamiento(request):
    return render(request, 'EquipoEntrenamiento.html')

def EvaluacionFisica(request):
    return render(request, 'EvaluacionFisica.html')

def Evento(request):
    return render(request,'Evento.html')

def Factura(request):
    return render(request, 'Factura.html')

def InsumoDeportivo(request):
    return render(request, 'InsumoDeportivo.html')

def Membresia(request):
    return render(request, 'Membresia.html')

def Pago(request):
    return render(request, 'Pago.html') 

def PlanNutricional(request):
    return render(request, 'PlanNutricional.html')

def ProgramaEntrenamiento(request):
    return render(request, 'ProgramaEntrenamiento.html') 

def Promocion(request):
    return render(request, 'Promocion.html')

def Publicacion(request):
    return render(request, 'Publicacion.html') 

def RutinaEntrenamiento(request):
    return render(request, 'RutinaEntrenamiento.html')

def Sucursal(request):
    return render(request, 'Sucursal.html') 

def TransaccionInsumo(request):
    return render(request, 'TransaccionInsumo.html')
# Iniciar sesión
def signIn(request):
    return render(request, 'accounts/signin.html')
# Registrarse
def signUp (request):
    print(request.GET)
    return render (request, 'accounts/signup.html', {
        'form': newCreateClientForm
    })
