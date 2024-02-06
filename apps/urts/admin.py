from django.contrib import admin
from apps.urts.models import URTs

class URTsAdmin(admin.ModelAdmin):
    list_display = ('municipio', 'uf', 'nome_propriedade', 'proprietario_nome', 'area_experimento', 'registro_data', 'ult_atual_data')
    list_filter = ('uf', 'municipio', 'textura_solo', 'local_preparo_amostras')
    search_fields = ('nome_propriedade', 'proprietario_nome', 'municipio')
    readonly_fields = ('registro_data', 'ult_atual_data', 'log_n_edicoes')

    # def save_model(self, request, obj, form, change):
    #     if not obj.pk:
    #         # Somente para novos objetos
    #         obj.usuario_registro = request.user
    #     obj.usuario_atualizacao = request.user
    #     super().save_model(request, obj, form, change)

    def soft_delete_model(self, request, queryset):
        for obj in queryset:
            obj.soft_delete(request.user)

    actions = [soft_delete_model]

admin.site.register(URTs, URTsAdmin)

