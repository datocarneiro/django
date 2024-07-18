from django.shortcuts import render
from results.post import posts


# Create your views here.
def home(request):
    data = posts()
    context= {
        'title': 'Pagina de RESULTADOS',
        'posts': data
        }
    return render(request, 'results/index.html', context)

def clientes_ativos(request):
    return render(request, 'results/clientesAtivos.html')

def clientes_desativados(request):
    return render(request, 'results/clientesDesativados.html')

