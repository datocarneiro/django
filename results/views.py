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

def post(request, post_id):
    data = posts()
    _id = int(post_id)
    print('PostID:',post_id)
    for i in data:
        if i['id'] == _id:
            break
    print('*********************************************')
    print('print iiiiiiii:', _id, i['id'], i['title'])
    context= {
        'texto_principal': 'Post ID: ',
        'post_id': _id,
        'post': i
        }
        
    return render(request, 'results/post_id.html', context)

def clientes_ativos(request):
    return render(request, 'results/clientesAtivos.html')

def clientes_desativados(request):
    return render(request, 'results/clientesDesativados.html')

