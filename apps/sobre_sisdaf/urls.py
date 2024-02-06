from django.contrib import admin
from django.urls import path
from apps.sobre_sisdaf.views import sisdaf_ajuda, sisdaf_banco_dados, sisdaf_sugestoes, sisdaf_versoes

urlpatterns = [
    
    path('sobre-sisdaf/ajuda', sisdaf_ajuda, name='sisdaf_ajuda'),
    path('sobre-sisdaf/banco-dados', sisdaf_banco_dados, name='sisdaf_banco_dados'),
    path('sobre-sisdaf/sugestoes', sisdaf_sugestoes, name='sisdaf_sugestoes'),
    path('sobre-sisdaf/versoes', sisdaf_versoes, name='sisdaf_versoes'),
    
]