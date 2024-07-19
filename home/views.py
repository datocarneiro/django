from django.shortcuts import render

# Create your views here.
def home(request):

    context = {
        'texto_principal': 'block texto_principal',
        'title': 'Pagina Home'
    }

    return render(
        request, 
        'home/index.html',
        context
)

