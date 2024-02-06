from django.contrib import admin
from django.urls import path
from apps.programacao.views import prog_basico
from apps.programacao.views import prog_especializado, prog_especializado_ficha_prog
from apps.programacao.views import prog_estrategico

urlpatterns = [

    #COMPONENTE BASICO
    path('programacao/basico/', prog_basico, name='prog_basico'),

    #COMPONENTE ESPECIALIZADO
    path('programacao/especializado/', prog_especializado, name='prog_especializado'),
    path('programacao/especializado/ficha/programacao/', prog_especializado_ficha_prog, name='prog_especializado_ficha_prog'),

    #COMPONENTE ESTRATEGICO
    path('programacao/estrategico/', prog_estrategico, name='prog_estrategico'),

]