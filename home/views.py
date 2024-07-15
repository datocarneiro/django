from django.shortcuts import render

# Create your views here.
def home(request):

    context = {
        'mensagem1': 'MSG - 001',
        'mensagem2': 'AQUI OUTRA MENSAGEM - 002',
        'title': 'Pagina Home'
    }

    return render(
        request, 
        'home/index.html',
        context
)

