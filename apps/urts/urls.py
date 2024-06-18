from django.contrib import admin
from django.urls import path
from apps.urts.views import (urts, urt_ficha, 
                             especie_vegetal_salvar, especie_vegetal_modal, especie_vegetal_deletar,
                             especie_animal_salvar, especie_animal_modal, especie_animal_deletar,
                             tecnico_salvar, tecnico_modal, tecnico_deletar,
                             urt_relatorio_ficha, listagem_ciclos_urt, ciclo_urt_ficha
                             )


urlpatterns = [
    
    #URTs
    path('urts/', urts, name='urts'),

    #FICHA DA URT
    path('urts/ficha/<int:urt_id>/', urt_ficha, name='urt_ficha'),
    path('urts/ficha/salvar/<int:urt_id>/', urt_ficha, name='urt_ficha'),

    #ESPÉCIE VEGETAL
    path('urts/ficha/especie-vegetal/<int:vegetal_id>/dados/', especie_vegetal_modal, name='especie_vegetal_modal'),
    path('urts/ficha/especie-vegetal/salvar/novo/', especie_vegetal_salvar, name='especie_vegetal_salvar_novo'),
    path('urts/ficha/especie-vegetal/salvar/<int:vegetal_id>/', especie_vegetal_salvar, name='especie_vegetal_salvar'),
    path('urts/ficha/especie-vegetal/deletar/<int:vegetal_id>/', especie_vegetal_deletar, name='especie_vegetal_deletar'),

    #ESPÉCIE ANIMAL
    path('urts/ficha/especie-animal/<int:animal_id>/dados/', especie_animal_modal, name='especie_animal_modal'),
    path('urts/ficha/especie-animal/salvar/novo/', especie_animal_salvar, name='especie_animal_salvar_novo'),
    path('urts/ficha/especie-animal/salvar/<int:animal_id>/', especie_animal_salvar, name='especie_animal_salvar'),
    path('urts/ficha/especie-animal/deletar/<int:animal_id>/', especie_animal_deletar, name='especie_animal_deletar'),

    #TECNICOS DA URT
    path('urts/ficha/tecnico/<int:tecnico_id>/dados/', tecnico_modal, name='tecnico_modal'),
    path('urts/ficha/tecnico/salvar/novo/', tecnico_salvar, name='tecnico_salvar_novo'),
    path('urts/ficha/tecnico/salvar/<int:tecnico_id>/', tecnico_salvar, name='tecnico_salvar'),
    path('urts/ficha/tecnico/deletar/<int:tecnico_id>/', tecnico_deletar, name='tecnico_deletar'),

    #CICLOS DA URT
    path('urts/ficha/ciclo/', listagem_ciclos_urt, name='listagem_ciclos_urt'),
    path('urts/ficha/ciclo/ficha/', ciclo_urt_ficha, name='ciclo_urt_ficha'),


    #RELATÓRIOS
    path('urts/relatorio/ficha-urt/<int:urt_id>/', urt_relatorio_ficha, name='urt_relatorio_ficha'),

]