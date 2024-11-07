from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Página inicial
    path('calcular/', views.calcular_emissoes, name='calcular_emissoes'),
]
