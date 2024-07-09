from django.urls import path
# Importando as views do app 'results' e renomeando para 'views_results'
from results import views as views_results 

urlpatterns = [
    # Rota para a página inicial dos resultados
    path('', views_results.home),      
    # Rota para a página de clientes ativos
    path('clientesAtivos/', views_results.clientes_ativos),      
    # Rota para a página de clientes desativados
    path('clientesDesativados/', views_results.clientes_desativados),  
]
