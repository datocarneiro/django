from django.shortcuts import render

# Create your views here.
def home(request):

    context= {'title': 'Pagina de RESULTADOS'}
    return render(request, 'results/index.html', context)

def clientes_ativos(request):
    return render(request, 'results/clientesAtivos.html')

def clientes_desativados(request):
    return render(request, 'results/clientesDesativados.html')

