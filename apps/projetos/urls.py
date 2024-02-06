from django.contrib import admin
from django.urls import path
from apps.projetos.views import projetos, projeto_ficha, projetos_filtrar
from apps.projetos.views import projeto_execfin


urlpatterns = [
    
    #PROJETOS
    path('projetos/', projetos, name='projetos'),
    path('projetos/filtro/', projetos_filtrar, name='projetos_filtrar'),

    #DADOS GERAIS
    path('projetos/ficha/dados-gerais/novo/', projeto_ficha, name='projeto_novo'),
    path('projetos/ficha/dados-gerais/<int:id_projeto>/', projeto_ficha, name='projeto_ficha'),

    #EXECUCAO FINANCEIRA
    path('projetos/ficha/execucao-financeira/novo/', projeto_execfin, name='projeto_execfin_novo'),
    path('projetos/ficha/execucao-financeira/<int:id_projeto>/', projeto_execfin, name='projeto_execfin'),
    
]