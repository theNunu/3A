from django.contrib import admin
from .models import Cliente, Pago, Sucursal, DetalleCliente, InsumoDeportivo, Membresia, EquipoEntrenamiento, Entrenador, Comentario, RutinaEntrenamiento, EvaluacionFisica, Promocion, PlanNutricional, TransaccionInsumo, Evento, Factura, Publicacion, ProgramaEntrenamiento, Empleado

# Registrar modelos en el admin
admin.site.register(Cliente)
admin.site.register(Pago)
admin.site.register(Sucursal)
admin.site.register(DetalleCliente)
admin.site.register(InsumoDeportivo)
admin.site.register(Membresia)
admin.site.register(EquipoEntrenamiento)
admin.site.register(Entrenador)
admin.site.register(Comentario)
admin.site.register(RutinaEntrenamiento)
admin.site.register(EvaluacionFisica)
admin.site.register(Promocion)
admin.site.register(PlanNutricional)
admin.site.register(TransaccionInsumo)
admin.site.register(Evento)
admin.site.register(Factura)
admin.site.register(Publicacion)
admin.site.register(ProgramaEntrenamiento)
admin.site.register(Empleado)
