from django.contrib import admin
from django.urls import path
from apps.produtos.views import produtos, produtos_ficha, produtos_cmm, get_filtros_produtos, exportar_produtos, delete_produto, salvar_tags, produto_exportar_pdf
from apps.produtos.views import denominacoes, denominacoes_ficha, get_filtros_denominacoes, exportar_denominacoes, delete_denominacao
from apps.produtos.views import denominacoes_buscar

urlpatterns = [
    
    #denominacoes
    path('produtosdaf/buscardenominacoes/<str:unidade_daf>/', denominacoes_buscar, name='denominacoes_buscar'),
    path('produtosdaf/denominacoes/ficha/novo/', denominacoes_ficha, name='nova_denominacao'),
    path('produtosdaf/denominacoes/ficha/<int:denominacao_id>/', denominacoes_ficha, name='denominacoes_ficha'),
    path('produtosdaf/denominacoes/deletar/<int:denominacao_id>/', delete_denominacao, name='delete_denominacao'),
    path('produtosdaf/denominacoes/filtro/', get_filtros_denominacoes, name='get_filtros_denominacoes'),
    path('produtosdaf/denominacoes/exportar/', exportar_denominacoes, name='exportar_denominacoes'),
    path('produtosdaf/denominacoes', denominacoes, name='denominacoes'),
    
    #produtos
    path('produtosdaf/produtos/ficha/cmm/<int:product_id>/', produtos_cmm, name='produtos_cmm'),
    path('produtosdaf/produtos/pdf/<int:product_id>/', produto_exportar_pdf, name='produto_exportar_pdf'),
    path('produtosdaf/produtos/ficha/novo/', produtos_ficha, name='novo_produto'),
    path('produtosdaf/produtos/ficha/<int:product_id>/', produtos_ficha, name='produtos_ficha'),
    path('produtosdaf/produtos/deletar/<int:product_id>/', delete_produto, name='delete_produto'),
    path('produtosdaf/produtos/filtro/', get_filtros_produtos, name='get_filtros_produtos'),
    path('produtosdaf/produtos/exportar/', exportar_produtos, name='exportar_produtos'),
    path('produtosdaf/produtos/salvartags/<int:product_id>/', salvar_tags, name='salvar_tags'),
    path('produtosdaf/produtos', produtos, name='produtos'),
    
]