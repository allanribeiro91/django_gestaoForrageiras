from django.contrib import admin
from apps.fornecedores.models import Fornecedores, Fornecedores_Faq, Fornecedores_Representantes, Fornecedores_Comunicacoes

class FornecedoresAdmin(admin.ModelAdmin):
    list_display = ('id', 'cnpj', 'nome_fantasia', 'tipo_direito', 'hierarquia', 'porte', 'end_uf', 'end_municipio', 'del_status')
    list_display_links = ("id","cnpj", "nome_fantasia")
    search_fields = ('cnpj', 'nome_fantasia')
    ordering = ('nome_fantasia',)
    list_filter = ('tipo_direito', 'hierarquia', 'porte', 'end_uf')
    list_per_page = 100

class FornecedoresFaqAdmin(admin.ModelAdmin):
    list_display = ('id', 'topico', 'contexto', 'resposta', 'observacoes_gerais', 'del_status')
    list_display_links = ('id', 'topico')
    search_fields = ('topico', 'contexto', 'resposta')
    list_filter = ('topico',)
    list_per_page = 100

class FornecedoresRepresentantesAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_completo', 'cpf', 'cargo', 'telefone', 'celular', 'email', 'del_status')
    list_display_links = ('id', 'nome_completo')
    search_fields = ('nome_completo', 'cpf', 'cargo')
    list_filter = ('cargo', 'genero_sexual')
    list_per_page = 100

class FornecedoresComunicacoesAdmin(admin.ModelAdmin):
    list_display = ('id', 'unidade_daf', 'tipo_comunicacao', 'topico_comunicacao', 'assunto', 'status_envio', 'del_status')
    list_display_links = ('id', 'unidade_daf')
    search_fields = ('unidade_daf', 'tipo_comunicacao', 'topico_comunicacao', 'assunto')
    list_filter = ('unidade_daf', 'tipo_comunicacao', 'status_envio')
    list_per_page = 100

admin.site.register(Fornecedores, FornecedoresAdmin)
admin.site.register(Fornecedores_Faq, FornecedoresFaqAdmin)
admin.site.register(Fornecedores_Representantes, FornecedoresRepresentantesAdmin)
admin.site.register(Fornecedores_Comunicacoes, FornecedoresComunicacoesAdmin)
