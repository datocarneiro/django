from django.urls import path
from home import views as views_home

urlpatterns = [
    path('', views_home.home, name='home'),
]