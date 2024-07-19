from django.urls import path

# Importando as views do app 'results' e renomeando para 'views_results'
from results import views as views_results 
app_name = 'results'


urlpatterns = [
    # Rota para a página de clientes desativados
    path('clientesDesativados/', views_results.clientes_desativados, name='clientesDesativados'), 
    # Rota para a página de clientes ativos
    path('clientesAtivos/', views_results.clientes_ativos, name='clientesAtivos'),      
    # Rota para a página com post especifico com o ID
    path('post/<post_id>/', views_results.post, name='post_id'),      
    # Rota para a página com todos os posts
    path('', views_results.home, name='results/home'),      
]
