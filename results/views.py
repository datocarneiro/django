from django.shortcuts import render
from results.post import posts
# Create your views here.
def home(request):

    context= {
        'title': 'Pagina de RESULTADOS',
        'posts': posts()
        }
    for post in context['posts']:
        print(post['id'])
    return render(request, 'results/index.html', context)

def clientes_ativos(request):
    return render(request, 'results/clientesAtivos.html')

def clientes_desativados(request):
    return render(request, 'results/clientesDesativados.html')

