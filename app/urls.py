from django.urls import path
from . import views

urlpatterns = [
   path('',views.home),
   #pages
   path('clientes/', views.clientes),
   path('sucursales/', views.sucursales),
   path('ti/', views.ti),
]

