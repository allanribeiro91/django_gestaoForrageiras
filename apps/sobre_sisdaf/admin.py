from django.contrib import admin
from apps.sobre_sisdaf.models import VersoesSisdaf

class VersoesSisdafAdmin(admin.ModelAdmin):
    list_display = ('id', 'versao', 'status', 'data_versao', 'informacoes')
    list_display_links = ('id', 'versao', 'status', 'data_versao', 'informacoes')
    search_fields = ('versao', 'data_versao')
    ordering = ('versao',)
    list_per_page = 100

admin.site.register(VersoesSisdaf, VersoesSisdafAdmin)