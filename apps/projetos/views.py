from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage
from django.urls import reverse
from django.contrib import messages
from django.http import QueryDict
from apps.main.models import CustomLog
from apps.usuarios.models import Usuarios
from apps.projetos.models import Projetos
from apps.projetos.forms import ProjetosForm, FiltroProjetosForm, ProjetosAtividadesForm
from django.http import JsonResponse, HttpResponse
from datetime import datetime
from django.utils import timezone
import pytz

#timezone
tz = pytz.timezone("America/Sao_Paulo")

def projetos(request):
    tab_projetos = Projetos.objects.filter(del_status=False)
    form_filtro = FiltroProjetosForm()

    conteudo = {
        'tab_projetos': tab_projetos,
        'form_filtro': form_filtro,
    }
    return render(request, 'projetos/projetos.html', conteudo)

def projetos_filtrar(request):
    regional = request.GET.get('regional', None)
    status = request.GET.get('status', None)
    subprograma = request.GET.get('subprograma', None)
    data_inicio = request.GET.get('data_inicio', None)
    data_fim = request.GET.get('data_fim', None)
    nome_plano_trabalho = request.GET.get('nome_plano_trabalho', None)
    print('status: ', status)
    filters = {}
    filters['del_status'] = False
    if regional:
        filters['regional'] = regional
    if status:
        filters['status'] = status
    if subprograma:
        filters['subprograma'] = subprograma
    if data_inicio:
        filters['data_inicio'] = data_inicio
    if data_fim:
        filters['data_fim'] = data_fim
    if nome_plano_trabalho:
        filters['nome_plano_trabalho__icontains'] = nome_plano_trabalho
    
    tab_projetos = Projetos.objects.filter(**filters).order_by('nome_plano_trabalho')
    total_projetos = tab_projetos.count()
    
    projetos_formatados = []
    for projeto in tab_projetos:
        projetos_formatados.append({
            'id': projeto.id,
            'id_projeto_sisateg': projeto.id_projeto_sisateg,
            'regional': projeto.get_regional_display(),
            'status': projeto.get_status_display(),
            'subprograma': projeto.get_subprograma_display(),
            'nome_plano_trabalho': projeto.nome_plano_trabalho,
            'n_processo': projeto.n_processo,
            'data_inicio': projeto.data_inicio.strftime('%d/%m/%Y') if projeto.data_inicio else '',
            'data_fim': projeto.data_fim.strftime('%d/%m/%Y') if projeto.data_fim else '',
            'gestor_dateg': projeto.gestor_dateg.primeiro_ultimo_nome() if projeto.gestor_dateg else ''
        })

    
    page = int(request.GET.get('page', 1))
    paginator = Paginator(projetos_formatados, 100) 
    try:
        projetos_paginados = paginator.page(page)
    except EmptyPage:
        projetos_paginados = paginator.page(paginator.num_pages)
    
    return JsonResponse({
        'data': list(projetos_paginados.object_list),
        'total_projetos': total_projetos,
        'has_next': projetos_paginados.has_next(),
        'has_previous': projetos_paginados.has_previous(),
        'current_page': page
    })


#DADOS GERAIS
def projeto_ficha(request, id_projeto=None):
    if id_projeto:
        try:
            projeto = Projetos.objects.get(id=id_projeto)
        except projeto.DoesNotExist:
            messages.error(request, "Projeto não encontrado.")
            return redirect('projetos')
    else:
        projeto = None
    
    #salvar
    if request.method == 'POST':
        #Carregar formulário
        if projeto:
            projeto_form = ProjetosForm(request.POST, instance=projeto)
            novo_projeto = False
        else:
            projeto_form = ProjetosForm(request.POST)
            novo_projeto = True

        #Verificar se houve alteração no formulário
        if not projeto_form.has_changed():
            return JsonResponse({
                    'retorno': 'Não houve mudanças'
                })

        #Passar o objeto Denominação Genérica
        usuario_id = request.POST.get('gestor_dateg')
        usuario_instance = Usuarios.objects.get(id=usuario_id)
        
        #Fazer uma cópia mutável do request.POST
        modificacoes_post = QueryDict(request.POST.urlencode(), mutable=True)

        #Atualizar os valores no mutable_post
        modificacoes_post['gestor_dateg'] = usuario_instance

        #Criar o formulário com os dados atualizados
        projeto_form = ProjetosForm(modificacoes_post, instance=projeto_form.instance)

        #salvar
        if projeto_form.is_valid():
            #Salvar o produto
            projeto = projeto_form.save(commit=False)
            projeto.save(current_user=request.user.usuario_relacionado)
            
            #logs
            log_id = projeto.id
            log_registro_usuario = projeto.usuario_registro.nome_completo
            log_registro_data = projeto.registro_data.astimezone(tz).strftime('%d/%m/%Y %H:%M:%S')
            log_atualizacao_usuario = projeto.usuario_atualizacao.nome_completo
            log_atualizacao_data = projeto.ult_atual_data.astimezone(tz).strftime('%d/%m/%Y %H:%M:%S')
            log_edicoes = projeto.log_n_edicoes

            # Registrar a ação no CustomLog
            current_date_str = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
            log_entry = CustomLog(
                usuario=request.user.usuario_relacionado,
                modulo="Projetos_Dados Gerais",
                model='Projetos',
                model_id=projeto.id,
                item_id=0,
                item_descricao="Salvar edição de Projeto.",
                acao="Salvar",
                observacoes=f"Usuário {request.user.username} salvou o Projeto (ID {projeto.id}, Plano de Trabalho: {projeto.nome_plano_trabalho}, Regional: {projeto.regional}) em {current_date_str}."
            )
            log_entry.save()

            #Retornar
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({
                    'retorno': 'Salvo',
                    'log_id': log_id,
                    'log_registro_usuario': log_registro_usuario,
                    'log_registro_data': log_registro_data,
                    'log_atualizacao_usuario': log_atualizacao_usuario,
                    'log_atualizacao_data': log_atualizacao_data,
                    'log_edicoes': log_edicoes,
                    'novo': novo_projeto,
                    'redirect_url': reverse('projeto_ficha', args=[projeto.id]),
                })
        else:
            print("Erro formulário Projeto")
            print(projeto_form.errors)
            return JsonResponse({
                    'retorno': 'Erro ao salvar'
                })

    if projeto:
        form = ProjetosForm(instance=projeto)
    else:
        form = ProjetosForm()

    form_atividade = ProjetosAtividadesForm()

    conteudo = {
        'form': form,
        'projeto': projeto,
        'form_atividade': form_atividade,
    }

    return render(request, 'projetos/projeto_ficha.html', conteudo)


#EXECUCAO FINANCEIRA
def projeto_execfin(request, id_projeto=None):
    return render(request, 'projetos/projeto_execucao_financeira.html')