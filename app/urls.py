from django.urls import path
from . import views

urlpatterns = [
    path('', views.first),
    path('Cliente/', views.Cliente),
    path('Comentario/', views.Comentario),
    path('DetalleCliente/', views.DetalleCliente),
    path('Empleado/', views.Empleado),
    path('Entrenador/', views.Entrenador),
    path('EquipoEntrenamiento/', views.EquipoEntrenamiento),
    path('EvaluacionFisica/', views.EvaluacionFisica),
    path('Evento/', views.Evento),
    path('Factura/', views.Factura),
    path('InsumoDeportivo/', views.InsumoDeportivo),
    path('Membresia/', views.Membresia),
    path('Pago/', views.Pago),
    path('PlanNutricional/', views.PlanNutricional),
    path('ProgramaEntrenamiento/', views.ProgramaEntrenamiento),
    path('Promocion/', views.Promocion),
    path('Publicacion/', views.Publicacion),
    path('RutinaEntrenamiento/', views.RutinaEntrenamiento),
    path('Sucursal/', views.Sucursal),
    path('TransaccionInsumo/', views.TransaccionInsumo),
    path('login/', views.login)
    
]
