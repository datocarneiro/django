from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def results(request):
    print('estamos na View "RESULTS" do app Results')
    return HttpResponse('estamos na View "RESULTS" do app Results')

