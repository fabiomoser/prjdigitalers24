from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("acerca-de", views.acerca_de, name='acerca_de'),
    path("clientes", views.clientes, name="clientes"),
    path("cliente/<str:nombre_cliente>", views.cliente, name='cliente'),
    path("nuevo_cliente", views.nuevo_cliente, name='nuevo_cliente')
]