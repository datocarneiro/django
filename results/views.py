from django.shortcuts import render
from results.post import posts
from typing import Any
from django.http import HttpRequest, HttpResponse, Http404


# Create your views here.
def home(request):
    data = posts()
    context= {
        'title': 'Pagina de RESULTADOS',
        'posts': data
        }
    return render(request, 'results/index.html', context)

def post(request: HttpRequest, post_id:int):
    post_encontrado: dict[str, Any] | None = None
    print(type(post_id))


    data = posts()
    print('PostID:',post_id)

    for i in data:
        if i['id'] == int(post_id):
            post_encontrado = i
            break 

    if post_encontrado is None:
    
        raise Http404 ('Post, não existe')
    
    context= {
        'texto_principal': 'Post ID: ',
        'post_id': post_id,
        'post': post_encontrado
        }
        
    return render(request, 'results/post_id.html', context)

def clientes_ativos(request):
    return render(request, 'results/clientesAtivos.html')

def clientes_desativados(request):
    return render(request, 'results/clientesDesativados.html')
