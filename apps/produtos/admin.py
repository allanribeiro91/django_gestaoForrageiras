from django.contrib import admin
from apps.produtos.models import DenominacoesGenericas, ProdutosFarmaceuticos

class ListandoDenominacoes(admin.ModelAdmin):
    list_display = ("id", "tipo_produto", "denominacao", "unidade_basico", "unidade_especializado", "unidade_estrategico", "unidade_farm_popular", "hospitalar", "del_status")
    list_display_links = ("id","tipo_produto", "denominacao")
    list_filter = ("tipo_produto", "unidade_basico", "unidade_especializado", "unidade_estrategico", "unidade_farm_popular", "hospitalar")
    list_per_page = 100

class ListandoProdutos(admin.ModelAdmin):
    
    def tipo_produto(self, obj):
        return obj.denominacao.tipo_produto
    tipo_produto.short_description = 'Tipo de Produto'
    
    list_display = ("id", "tipo_produto", "produto", "comp_basico", "comp_especializado", "comp_estrategico", "disp_farmacia_popular", "hospitalar", "del_status")
    list_display_links = ("tipo_produto", "produto")
    list_filter = ("denominacao__tipo_produto", "comp_basico", "comp_especializado", "comp_estrategico", "disp_farmacia_popular", "hospitalar")
    list_per_page = 100


admin.site.register(ProdutosFarmaceuticos, ListandoProdutos)
admin.site.register(DenominacoesGenericas, ListandoDenominacoes)
