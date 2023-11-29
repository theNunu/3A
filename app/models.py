from django.db import models

#1
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=15)
    fecha_registro = models.DateField(auto_now_add=True)
#2
class Pago(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateTimeField(auto_now_add=True)
#3
class Sucursal(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.TextField()
    telefono = models.CharField(max_length=15)
#4
class DetalleCliente(models.Model):
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(max_length=10)
    altura = models.FloatField()
    peso = models.FloatField()
#5
class InsumoDeportivo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
#6
class Membresia(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio_mensual = models.DecimalField(max_digits=10, decimal_places=2)
    beneficios = models.TextField()
    duracion_meses = models.IntegerField()
#7
class EquipoEntrenamiento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
#8
class Entrenador(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
#9
class Comentario(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    texto = models.TextField()
    fecha_comentario = models.DateTimeField(auto_now_add=True)
#10
class RutinaEntrenamiento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    duracion_minutos = models.IntegerField()
    dificultad = models.CharField(max_length=20)
#11
class EvaluacionFisica(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_evaluacion = models.DateField()
    peso = models.FloatField()
    altura = models.FloatField()
    porcentaje_grasa = models.FloatField()
#12
class Promocion(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    descuento_porcentaje = models.DecimalField(max_digits=5, decimal_places=2)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
#13
class PlanNutricional(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
#14
class TransaccionInsumo(models.Model):
    insumo = models.ForeignKey(InsumoDeportivo, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fecha_transaccion = models.DateTimeField(auto_now_add=True)
#15
class Evento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
#16
class Factura(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_emision = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
#17
class Publicacion(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(Entrenador, on_delete=models.CASCADE)
#18
class ProgramaEntrenamiento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    duracion_semanas = models.IntegerField()
#19
class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    salario = models.DecimalField(max_digits=10, decimal_places=2)