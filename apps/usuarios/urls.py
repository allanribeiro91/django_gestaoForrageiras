from django.urls import path
from apps.usuarios.views import meusdados, meuslogs, meuslogs_exportar, meusacessos, meusacessos_exportar

urlpatterns = [
    path('usuario/meusdados/', meusdados, name='meusdados'),
    
    path('usuario/meuslogs/', meuslogs, name='meuslogs'),
    path('usuario/meuslogs/exportar/', meuslogs_exportar, name='meuslogs_exportar'),
    
    path('usuario/meusacessos/', meusacessos, name='meusacessos'),
    path('usuario/meusacessos/exportar/', meusacessos_exportar, name='meusacessos_exportar'),
]