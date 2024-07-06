"""
URL configuration for MeuProjetoDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Inclui as URLs do app 'home' na raiz do site
    path('', include('home.urls')),      
    # Inclui as URLs do app 'results' para a rota 'results_home'
    path('results_home/', include('results.urls')),      
    # Rota para a administração do site
    path('admin/', admin.site.urls),
]
