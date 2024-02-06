from django.contrib import admin
from django.urls import path
from apps.main.views import login, logout, home, cadastro, cadastro_confirmacao

urlpatterns = [
    path('', login, name='login'),
    path('logout', logout, name='logout'),
    path('home/', home, name='home'),
    path('cadastro/', cadastro, name='cadastro'),
    path('cadastro/confirmacao/', cadastro_confirmacao, name='cadastro_confirmacao'),
]