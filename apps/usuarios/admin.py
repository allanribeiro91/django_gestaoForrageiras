from django.contrib import admin
from apps.usuarios.models import Usuarios, Alocacoes
from apps.usuarios.forms import AlocacaoForm
from django.core.exceptions import ValidationError

@admin.register(Usuarios)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'cpf', 'data_nascimento', 'genero', 'cor_pele', 'usuario_is_ativo')
    search_fields = ('nome_completo', 'cpf')
    list_filter = ('genero', 'cor_pele', 'usuario_is_ativo')
    date_hierarchy = 'data_registro'
    ordering = ('data_registro', 'nome_completo')

@admin.register(Alocacoes)
class AlocacaoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'unidade', 'setor', 'data_inicio', 'data_fim', 'is_ativo')
    search_fields = ('usuario__nome_completo', 'usuario__cpf', 'setor')
    list_filter = ('unidade', 'is_ativo')
    date_hierarchy = 'data_registro'
    ordering = ('data_registro', 'usuario')

