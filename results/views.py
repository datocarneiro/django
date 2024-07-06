from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_results(request):
    return HttpResponse('estamos na View "RESULTS_HOME" do app Results')

def clientes_ativos(request):
    return HttpResponse('estamos na View "CLIENTES_ATIVOS" do app Results')

def clientes_desativados(request):
    return HttpResponse('estamos na View "CLIENTES_DESATIVADOS" do app Results')

