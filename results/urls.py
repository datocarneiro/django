from django.urls import path
from results import views as views_results

urlpatterns = [
    path('', views_results.home_results),
    path('clientes_ativos/', views_results.clientes_ativos),
    path('clientes_desativados/', views_results.clientes_desativados),
]