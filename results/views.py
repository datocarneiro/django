from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'results/index.html')

def clientes_ativos(request):
    return render(request, 'results/clientesAtivos.html')

def clientes_desativados(request):
    return render(request, 'results/clientesDesativados.html')

