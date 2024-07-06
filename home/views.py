from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    print('estamos na View "HOME" do app home')
    return HttpResponse('estamos na View "HOME" do app home')

