from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.sobre_sisdaf.models import VersoesSisdaf

@login_required
def sisdaf_ajuda(request):
    return render(request, 'sobre_sisdaf/ajuda.html')

@login_required
def sisdaf_banco_dados(request):
    return render(request, 'sobre_sisdaf/banco_dados.html')

@login_required
def sisdaf_sugestoes(request):
    return render(request, 'sobre_sisdaf/sugestoes.html')

@login_required
def sisdaf_versoes(request):
    tab_versoes = VersoesSisdaf.objects.all().filter(del_status=False).order_by('-versao')
    conteudo = {
        'tab_versoes': tab_versoes,
    }
    return render(request, 'sobre_sisdaf/versoes.html', conteudo)
