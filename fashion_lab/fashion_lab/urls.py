"""
URL configuration for fashion_lab project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.home, name='home'),
    path('armario/', views.armario, name='armario'),
    path('pergunta/', views.pergunta, name='pergunta'),
    path('cadastro_usuario/', views.cadastro_usuario, name='cadastro_usuario'),
    path('login_usuario/', views.login_usuario, name='login_usuario'),
    path('logout/', views.logout_usuario, name='logout_usuario'),
    path('cadastrar/partecima/', views.cadastra_parte_de_cima, name='cadastrar_parte_de_cima'),
    path('cadastrar/partebaixo/', views.cadastra_parte_de_baixo, name='cadastrar_parte_de_baixo'),
    path('cadastrar/calcado/', views.cadastra_calçado, name='cadastrar_calçado'),
    path('cadastrar/acessorio/', views.cadastra_acessorio, name='cadastrar_acessorio'),
]
