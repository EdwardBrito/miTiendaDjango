# tecnologia/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_productos, name='lista_productos'),  # Lista de productos
    path('agregar/', views.agregar_producto, name='agregar_producto'),  # Agregar producto
    path('eliminar/<int:id>/', views.eliminar_producto, name='eliminar_producto'),  # Eliminar producto
]
