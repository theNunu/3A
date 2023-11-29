from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Cliente, Pago, Sucursal, DetalleCliente, InsumoDeportivo, Membresia, EquipoEntrenamiento, Entrenador, Comentario, RutinaEntrenamiento, EvaluacionFisica, Promocion, PlanNutricional, TransaccionInsumo, Evento, Factura, Publicacion, ProgramaEntrenamiento, Empleado
from .forms import ClienteForm
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

#model cliente
class ClienteListView(ListView):
    model = Cliente
    template_name = 'tables/app-cliente/cliente/cliente_list.html'

class ClienteDetailView(DetailView):
    model = Cliente
    template_name = 'tables/app-cliente/cliente/cliente_detail.html'

class ClienteCreateView(CreateView):
    model = Cliente
    template_name = 'tables/app-cliente/cliente/cliente_form.html'
    form_class = ClienteForm
