from unicodedata import name
from django.urls import path
from .views import MenuInicial,Categoria,seguimiento,CarroCompra,Donaciones,inicioSesion,registro

urlpatterns = [
    path('', MenuInicial,name="Menu Inicial"),
    path('Categoria/', Categoria,name="Categoria"),
    path('seguimiento/', seguimiento,name="Seguimiento"),
    path('CarroCompra/', CarroCompra,name="Carro Compra"),
    path('Donaciones/', Donaciones,name="Donaciones"),
    path('inicioSesion/', inicioSesion,name="Iniciar Sesion"),
    path('registro/', registro,name="Registro"),
] 