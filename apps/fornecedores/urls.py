from django.contrib import admin
from django.urls import path
from apps.fornecedores.views import fornecedores, fornecedores_filtro, fornecedores_exportar, fornecedor_ficha, fornecedor_ficha_filtrar_dados, fornecedor_delete
from apps.fornecedores.views import fornecedores_faq, fornecedor_faq_ficha, fornecedor_faq_filtrar_dados, fornecedor_faq_delete, fornecedores_faq_exportar
from apps.fornecedores.views import fornecedor_representante_delete, fornecedores_representantes, representante_dados
from apps.fornecedores.views import fornecedor_representantes_exportar, fornecedor_comunicacao_delete, fornecedores_comunicacoes, comunicacao_dados, fornecedor_usuarios_por_unidade, fornecedor_comunicacao_exportar
from apps.fornecedores.views import fornecedores_buscar

urlpatterns = [

    #FAQ
    path('fornecedores/faq/ficha/deletar/<int:faq_id>/', fornecedor_faq_delete, name='fornecedor_faq_delete'),
    path('fornecedores/faq/filtrar_dados/', fornecedor_faq_filtrar_dados, name='fornecedor_faq_filtrar_dados'),
    path('fornecedores/faq/ficha/<int:faq_id>/', fornecedor_faq_ficha, name='fornecedor_faq_ficha'),
    path('fornecedores/faq/exportar/', fornecedores_faq_exportar, name='fornecedores_faq_exportar'),
    path('fornecedores/faq/novo/', fornecedor_faq_ficha, name='fornecedor_faq_novo'),
    path('fornecedores/faq/', fornecedores_faq, name='fornecedores_faq'),

    #REPRESENTANTES DO FORNECEDOR
    path('fornecedores/representantes/deletar/<int:representante_id>/', fornecedor_representante_delete, name='fornecedor_representante_delete'),
    path('fornecedores/representantes/<int:id_fornecedor>/', fornecedores_representantes, name='fornecedores_representantes'),
    path('fornecedores/representantes/<int:representante_id>/dados/', representante_dados, name='representante_dados'),
    path('fornecedores/representantes/exportar/<int:id_fornecedor>/', fornecedor_representantes_exportar, name='fornecedor_representantes_exportar'),
    
    #COMUNICACOES COM O FORNECEDOR
    path('fornecedores/comunicacoes/deletar/<int:comunicacao_id>/', fornecedor_comunicacao_delete, name='fornecedor_comunicacao_delete'),
    path('fornecedores/comunicacoes/<int:id_fornecedor>/', fornecedores_comunicacoes, name='fornecedores_comunicacoes'),
    path('fornecedores/comunicacoes/<int:comunicacao_id>/dados/', comunicacao_dados, name='comunicacao_dados'),
    path('fornecedores/comunicacoes/exportar/<int:id_fornecedor>/', fornecedor_comunicacao_exportar, name='fornecedor_comunicacao_exportar'),
    path('fornecedores/usuarios_unidadedaf/<str:unidade>/', fornecedor_usuarios_por_unidade, name='fornecedor_usuarios_por_unidade'),

    #DADOS DO FORNECEDOR
    path('fornecedores/buscarfornecedores/', fornecedores_buscar, name='fornecedores_buscar'),
    path('fornecedores/ficha/deletar/<int:fornecedor_id>/', fornecedor_delete, name='fornecedor_delete'),
    path('fornecedores/ficha/filtrar_dados', fornecedor_ficha_filtrar_dados, name='fornecedor_ficha_filtrar_dados'),
    path('fornecedores/ficha/<int:fornecedor_id>/', fornecedor_ficha, name='fornecedor_ficha'),
    path('fornecedores/exportar/', fornecedores_exportar, name='fornecedores_exportar'),
    path('fornecedores/ficha/novo/', fornecedor_ficha, name='fornecedor_novo'),
    path('fornecedores/filtro/', fornecedores_filtro, name='fornecedores_filtro'),
    path('fornecedores/', fornecedores, name='fornecedores'),

]