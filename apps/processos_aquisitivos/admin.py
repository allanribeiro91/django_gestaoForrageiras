from django.contrib import admin
from .models import (ProaqDadosGerais, ProaqProdutos, ProaqEvolucao, ProaqTramitacao)

@admin.register(ProaqDadosGerais)
class ProaqDadosGeraisAdmin(admin.ModelAdmin):
    list_display = ('id', 'numero_processo_sei', 'unidade_daf', 'modalidade_aquisicao', 'status', 'get_usuario_nome')
    list_display_links = ('id', 'numero_processo_sei')
    search_fields = ('numero_processo_sei', 'unidade_daf', 'modalidade_aquisicao')
    list_filter = ('unidade_daf', 'modalidade_aquisicao', 'status')
    list_per_page = 100

@admin.register(ProaqProdutos)
class ProaqProdutosAdmin(admin.ModelAdmin):
    list_display = ('id', 'produto', 'proaq', 'del_status')
    list_display_links = ('id', 'produto')
    search_fields = ('produto__produto', 'proaq__numero_processo_sei')
    list_filter = ('del_status',)
    list_per_page = 100

@admin.register(ProaqEvolucao)
class ProaqEvolucaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'proaq', 'fase', 'status', 'data_inicio', 'data_fim', 'del_status')
    list_display_links = ('id', 'proaq')
    search_fields = ('proaq__numero_processo_sei', 'fase', 'status')
    list_filter = ('fase', 'status', 'del_status')
    list_per_page = 100

@admin.register(ProaqTramitacao)
class ProaqTramitacaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'proaq', 'documento_sei', 'setor', 'etapa_processo', 'del_status')
    list_display_links = ('id', 'documento_sei')
    search_fields = ('documento_sei', 'setor', 'etapa_processo')
    list_filter = ('setor', 'etapa_processo', 'del_status')
    list_per_page = 100
