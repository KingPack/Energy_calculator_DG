from django.urls import path

from . import views

urlpatterns = [
    path('calculator/', views.energy_calculator_view),
    path('create_cliente/', views.create_cliente),
    path('filter_clientes/', views.cliente_filter)
]