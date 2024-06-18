from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage
from django.urls import reverse
from django.http import QueryDict
from apps.main.models import CustomLog
from apps.usuarios.models import Usuarios
from apps.urts.models import URTs, URTespecieVegetal, URTespecieAnimal, TecnicoURT
from apps.urts.forms import URTsForm, URTespecieVegetalForm, URTespecieAnimalForm, TecnicoURTForm
from django.http import JsonResponse, HttpResponse
from datetime import datetime
from django.utils import timezone
import pytz

#timezone
tz = pytz.timezone("America/Sao_Paulo")

def urts(request):
    tab_urts = URTs.objects.all()
    conteudo = {
        'tab_urts': tab_urts,
    }
    return render(request, 'urts/urts.html', conteudo)


#FICHA DA URT
def urt_ficha(request, urt_id=None):

    if urt_id:
        urt = URTs.objects.get(id=urt_id)
        form_urt = URTsForm(instance=urt)
        tab_especies_vegetais = URTespecieVegetal.objects.filter(del_status=False, urt=urt_id)
        tab_especies_animais = URTespecieAnimal.objects.filter(del_status=False, urt=urt_id)
        tab_tecnicos = TecnicoURT.objects.filter(del_status=False, urt=urt_id)
    else:
        urt = None
        form_urt = URTsForm()
        tab_especies_vegetais = None
        tab_especies_animais = None
        tab_tecnicos = None
    
    #salvar
    if request.method == 'POST':
        #Carregar formulário
        if urt:
            urt_form = URTsForm(request.POST, instance=urt)
            nova_urt = False
        else:
            urt_form = URTsForm(request.POST)
            nova_urt = True
        
        #Verificar se houve alteração no formulário
        if not urt_form.has_changed():
            return JsonResponse({
                    'retorno': 'Não houve mudanças'
                })
        
        #salvar
        if urt_form.is_valid():
            #Salvar o produto
            urt = urt_form.save(commit=False)
            urt.save(current_user=request.user.usuario_relacionado)
            # Registrar a ação no CustomLog
            current_date_str = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
            observacoes = (
                f"Usuário {request.user.username} salvou dados da {urt}"
                f"({urt.id}) "
                f"em {current_date_str}."
            )
            
            log_entry = CustomLog(
                usuario=request.user.usuario_relacionado,
                modulo="URTs",
                model='URTs',
                model_id=urt.id,
                item_id=0,
                item_descricao="Salvar edição de dados da URT.",
                acao="Salvar",
                observacoes=observacoes
            )
            log_entry.save()
            
            #Retornar
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({
                    'retorno': 'Salvo',
                    'novo': nova_urt,
                })
        else:
            print("Erro formulário URT.")
            print(urt_form.errors)
            return JsonResponse({
                    'retorno': 'Erro ao salvar'
                })
        
    form_especie_animal = URTespecieAnimalForm()
    form_especie_vegetal = URTespecieVegetalForm()
    form_tecnico = TecnicoURTForm()

    conteudo = {
        'form_urt': form_urt,
        'urt': urt,
        'form_especie_animal': form_especie_animal,
        'form_especie_vegetal': form_especie_vegetal,
        'tab_especies_vegetais': tab_especies_vegetais,
        'tab_especies_animais': tab_especies_animais,
        'form_tecnico': form_tecnico,
        'tab_tecnicos': tab_tecnicos,
    }

    return render(request, 'urts/urt_ficha.html', conteudo)


#ESPÉCIE VEGETAL
def especie_vegetal_salvar(request, vegetal_id=None):
    if vegetal_id:
        especie_vegetal = URTespecieVegetal.objects.get(id=vegetal_id)
    else:
        especie_vegetal = None
    
    #salvar
    if request.method == 'POST':
        #Carregar formulário
        if especie_vegetal:
            especie_vegetal_form = URTespecieVegetalForm(request.POST, instance=especie_vegetal)
            novo_vegetal = False
        else:
            especie_vegetal_form = URTespecieVegetalForm(request.POST)
            novo_vegetal = True

        #Verificar se houve alteração no formulário
        if not especie_vegetal_form.has_changed():
            return JsonResponse({
                    'retorno': 'Não houve mudanças'
                })

        #Fazer uma cópia mutável do request.POST
        modificacoes_post = QueryDict(request.POST.urlencode(), mutable=True)

        #Instanciar a URT
        urt_id = request.POST.get('id_urt_vegetal')
        urt_instance = URTs.objects.get(id=urt_id)

        #Transformar o valor da área
        area_utilizada_str  = request.POST.get('area_utilizada')
        area_utilizada_str = area_utilizada_str.replace(',', '.')
        area_utilizada = float(area_utilizada_str)

        #Atualizar os valores no mutable_post
        modificacoes_post['urt'] = urt_instance
        modificacoes_post['area_utilizada'] = area_utilizada

        #Criar o formulário com os dados atualizados
        especie_vegetal_form = URTespecieVegetalForm(modificacoes_post, instance=especie_vegetal_form.instance)

        #salvar
        if especie_vegetal_form.is_valid():
            #Salvar o produto
            especie_vegetal = especie_vegetal_form.save(commit=False)
            especie_vegetal.save(current_user=request.user.usuario_relacionado)

            # Registrar a ação no CustomLog
            current_date_str = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
            log_entry = CustomLog(
                usuario=request.user.usuario_relacionado,
                modulo="URTs_Especies_Vegetais",
                model='URTespecieVegetal',
                model_id=especie_vegetal.id,
                item_id=0,
                item_descricao="Salvar edição de dados de Espécies Vegetais.",
                acao="Salvar",
                observacoes=f"Usuário {request.user.username} salvou a Espécie Vegetal (ID {especie_vegetal.id}, Espécie: {especie_vegetal.especie_vegetal}, Variedades: {especie_vegetal.variedades}) em {current_date_str}."
            )
            log_entry.save()

            #Retornar
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({
                    'retorno': 'Salvo',
                    'novo': novo_vegetal,
                    'especie_vegetal_id': especie_vegetal.id,
                })
        else:
            print("Erro formulário Espécie Vegetal.")
            print(especie_vegetal_form.errors)
            return JsonResponse({
                    'retorno': 'Erro ao salvar'
                })

def especie_vegetal_modal(request, vegetal_id=None):
    try:
        item = URTespecieVegetal.objects.get(id=vegetal_id)
        data = {
            #log
            'id': item.id,
            'log_data_registro': item.registro_data.strftime('%d/%m/%Y %H:%M:%S') if item.registro_data else '',
            'log_responsavel_registro': str(item.usuario_atualizacao.nome_completo),
            'lot_ult_atualizacao': item.ult_atual_data.strftime('%d/%m/%Y %H:%M:%S') if item.ult_atual_data else '',
            'log_responsavel_atualizacao': str(item.usuario_atualizacao.nome_completo),
            'log_edicoes': item.log_n_edicoes,
            
            #item
            'especie_vegetal': item.especie_vegetal,
            'variedades': item.variedades,
            'area_utilizada': item.area_utilizada,
            'producao_silagem': item.producao_silagem,

            #observações
            'observacoes': item.observacoes_gerais,

            #campos ocultos
            'urt_id': item.urt.id,

        }
        return JsonResponse(data)
    except URTespecieVegetal.DoesNotExist:
        return JsonResponse({'error': 'Espécie Vegetal não encontrada'}, status=404)

def especie_vegetal_deletar(request, vegetal_id=None):   
    try:
        item = URTespecieVegetal.objects.get(id=vegetal_id)
        item.soft_delete(request.user.usuario_relacionado)

        # Registrar a ação no CustomLog
        current_date_str = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        log_entry = CustomLog(
            usuario=request.user.usuario_relacionado,
            modulo="URTs_Especies_Vegetais",
            model='URTespecieVegetal',
            model_id=item.id,
            item_id=0,
            item_descricao="Deleção de Espécie Vegetal.",
            acao="Deletar",
            observacoes=f"Usuário {request.user.username} deletou a Espécie Vegetal (ID {item.id}, Espécie Vegetal: {item.get_especie_vegetal_display}) em {current_date_str}."
        )
        log_entry.save()

        return JsonResponse({
            "message": "Espécie Vegetal deletada com sucesso!"
            })
    except URTespecieVegetal.DoesNotExist:
        return JsonResponse({
            "message": "Espécie Vegetal não encontrada."
            })


#ESPÉCIE ANIMAL
def especie_animal_salvar(request, animal_id=None):
    if animal_id:
        especie_animal = URTespecieAnimal.objects.get(id=animal_id)
    else:
        especie_animal = None
    
    #salvar
    if request.method == 'POST':
        #Carregar formulário
        if especie_animal:
            especie_animal_form = URTespecieAnimalForm(request.POST, instance=especie_animal)
            novo_animal = False
        else:
            especie_animal_form = URTespecieAnimalForm(request.POST)
            novo_animal = True

        #Verificar se houve alteração no formulário
        if not especie_animal_form.has_changed():
            return JsonResponse({
                    'retorno': 'Não houve mudanças'
                })

        #Fazer uma cópia mutável do request.POST
        modificacoes_post = QueryDict(request.POST.urlencode(), mutable=True)

        #Instanciar a URT
        urt_id = request.POST.get('id_urt_animal')
        urt_instance = URTs.objects.get(id=urt_id)

        #Transformar o valor da área
        area_utilizada_str  = request.POST.get('area_utilizada')
        area_utilizada_str = area_utilizada_str.replace(',', '.')
        area_utilizada = float(area_utilizada_str)

        #Atualizar os valores no mutable_post
        modificacoes_post['urt'] = urt_instance
        modificacoes_post['area_utilizada'] = area_utilizada

        #Criar o formulário com os dados atualizados
        especie_animal_form = URTespecieAnimalForm(modificacoes_post, instance=especie_animal_form.instance)

        #salvar
        if especie_animal_form.is_valid():
            #Salvar o produto
            especie_animal = especie_animal_form.save(commit=False)
            especie_animal.save(current_user=request.user.usuario_relacionado)

            # Registrar a ação no CustomLog
            current_date_str = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
            log_entry = CustomLog(
                usuario=request.user.usuario_relacionado,
                modulo="URTs_Especies_Vegetais",
                model='URTespecieVegetal',
                model_id=especie_animal.id,
                item_id=0,
                item_descricao="Salvar edição de dados de Espécies Vegetais.",
                acao="Salvar",
                observacoes=f"Usuário {request.user.username} salvou a Espécie Vegetal (ID {especie_animal.id}, Espécie: {especie_animal.get_especie_animal_display}, Raças: {especie_animal.racas}) em {current_date_str}."
            )
            log_entry.save()

            #Retornar
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({
                    'retorno': 'Salvo',
                    'novo': novo_animal,
                    'especie_animal_id': especie_animal.id,
                })
        else:
            print("Erro formulário Espécie Animal.")
            print(especie_animal_form.errors)
            return JsonResponse({
                    'retorno': 'Erro ao salvar'
                })

def especie_animal_modal(request, animal_id=None):
    try:
        item = URTespecieAnimal.objects.get(id=animal_id)
        data = {
            #log
            'id': item.id,
            'log_data_registro': item.registro_data.strftime('%d/%m/%Y %H:%M:%S') if item.registro_data else '',
            'log_responsavel_registro': str(item.usuario_atualizacao.nome_completo),
            'lot_ult_atualizacao': item.ult_atual_data.strftime('%d/%m/%Y %H:%M:%S') if item.ult_atual_data else '',
            'log_responsavel_atualizacao': str(item.usuario_atualizacao.nome_completo),
            'log_edicoes': item.log_n_edicoes,
            
            #item
            'especie_animal': item.especie_animal,
            'racas': item.racas,
            'area_utilizada': item.area_utilizada,

            #observações
            'observacoes': item.observacoes_gerais,

            #campos ocultos
            'urt_id': item.urt.id,

        }
        return JsonResponse(data)
    except URTespecieAnimal.DoesNotExist:
        return JsonResponse({'error': 'Espécie Animal não encontrada'}, status=404)

def especie_animal_deletar(request, animal_id=None):   
    try:
        item = URTespecieAnimal.objects.get(id=animal_id)
        item.soft_delete(request.user.usuario_relacionado)

        # Registrar a ação no CustomLog
        current_date_str = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        log_entry = CustomLog(
            usuario=request.user.usuario_relacionado,
            modulo="URTs_Especies_Animais",
            model='URTespecieAnimal',
            model_id=item.id,
            item_id=0,
            item_descricao="Deleção de Espécie Animal.",
            acao="Deletar",
            observacoes=f"Usuário {request.user.username} deletou a Esp. Animal (ID {item.id}, Espécie Animal: {item.get_especie_animal_display}) em {current_date_str}."
        )
        log_entry.save()

        return JsonResponse({
            "message": "Espécie Animal deletada com sucesso!"
            })
    except URTespecieVegetal.DoesNotExist:
        return JsonResponse({
            "message": "Espécie Animal não encontrada."
            })


#TÉCNICO URT
def tecnico_salvar(request, tecnico_id=None):
    if tecnico_id:
        tecnico = TecnicoURT.objects.get(id=tecnico_id)
    else:
        tecnico = None
    
    #salvar
    if request.method == 'POST':
        #Carregar formulário
        if tecnico:
            tecnico_form = TecnicoURTForm(request.POST, instance=tecnico)
            novo_tecnico = False
        else:
            tecnico_form = TecnicoURTForm(request.POST)
            novo_tecnico = True

        #Verificar se houve alteração no formulário
        if not tecnico_form.has_changed():
            return JsonResponse({
                    'retorno': 'Não houve mudanças'
                })

        #Fazer uma cópia mutável do request.POST
        modificacoes_post = QueryDict(request.POST.urlencode(), mutable=True)

        #Instanciar a URT
        urt_id = request.POST.get('id_urt_tecnico')
        urt_instance = URTs.objects.get(id=urt_id)

        #Atualizar os valores no mutable_post
        modificacoes_post['urt'] = urt_instance

        #Criar o formulário com os dados atualizados
        tecnico_form = TecnicoURTForm(modificacoes_post, instance=tecnico_form.instance)

        #salvar
        if tecnico_form.is_valid():
            #Salvar o produto
            tecnico = tecnico_form.save(commit=False)
            tecnico.save(current_user=request.user.usuario_relacionado)

            # Registrar a ação no CustomLog
            current_date_str = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
            log_entry = CustomLog(
                usuario=request.user.usuario_relacionado,
                modulo="URTs_Tecnicos",
                model='TecnicoURT',
                model_id=tecnico.id,
                item_id=0,
                item_descricao="Salvar edição de dados do Técnico da URT.",
                acao="Salvar",
                observacoes=f"Usuário {request.user.username} salvou dados do Técnico da URT (ID {tecnico.id}, CPF: {tecnico.cpf}, CNPJ: {tecnico.cnpj}, Técnico: {tecnico.tecnico}, URT: {tecnico.urt}) em {current_date_str}."
            )
            log_entry.save()

            #Retornar
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({
                    'retorno': 'Salvo',
                    'novo': novo_tecnico,
                    'tecnico_id': tecnico.id,
                })
        else:
            print("Erro formulário Técnico da URT.")
            print(tecnico_form.errors)
            return JsonResponse({
                    'retorno': 'Erro ao salvar'
                })

def tecnico_modal(request, tecnico_id=None):
    try:
        item = TecnicoURT.objects.get(id=tecnico_id)
        data = {
            #log
            'id': item.id,
            'log_data_registro': item.registro_data.strftime('%d/%m/%Y %H:%M:%S') if item.registro_data else '',
            'log_responsavel_registro': str(item.usuario_atualizacao.nome_completo),
            'lot_ult_atualizacao': item.ult_atual_data.strftime('%d/%m/%Y %H:%M:%S') if item.ult_atual_data else '',
            'log_responsavel_atualizacao': str(item.usuario_atualizacao.nome_completo),
            'log_edicoes': item.log_n_edicoes,
            
            #contrato
            'status_contrato': item.status_contrato,
            'numero_contrato': item.numero_contrato,
            'data_inicio': item.data_inicio,
            'data_fim': item.data_fim,

            #dados da empresa
            'cnpj': item.cnpj,
            'razao_social': item.razao_social,
            'nome_fantasia': item.nome_fantasia,

            #dados do técnico
            'cpf': item.cpf,
            'tecnico': item.tecnico,
            'formacao_tecnica': item.formacao_tecnica,
            'celular': item.celular,
            'email': item.email,

            #observações
            'observacoes': item.observacoes_gerais,

            #campos ocultos
            'urt_id': item.urt.id,

        }
        return JsonResponse(data)
    except URTespecieAnimal.DoesNotExist:
        return JsonResponse({'error': 'Técnico não encontrado'}, status=404)

def tecnico_deletar(request, tecnico_id=None):   
    try:
        item = TecnicoURT.objects.get(id=tecnico_id)
        item.soft_delete(request.user.usuario_relacionado)

        # Registrar a ação no CustomLog
        current_date_str = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        log_entry = CustomLog(
            usuario=request.user.usuario_relacionado,
            modulo="URTs_Técnicos",
            model='TecnicoURT',
            model_id=item.id,
            item_id=0,
            item_descricao="Deleção de Técnico da URT.",
            acao="Deletar",
            observacoes=f"Usuário {request.user.username} deletou dados do Técnico da URT (ID {item.id}, CPF: {item.cpf}, CNPJ: {item.cnpj}, Técnico: {item.tecnico}, URT: {item.urt}) em {current_date_str}."
            )
        log_entry.save()

        return JsonResponse({
            "message": "Técnico da URT deletado com sucesso!"
            })
    except URTespecieVegetal.DoesNotExist:
        return JsonResponse({
            "message": "Técnico da URT não encontrado."
            })


#CICLOS DA URT
def listagem_ciclos_urt(request, id_urt=None):
    return render(request, 'urts/urt_listagem_ciclos.html')

def ciclo_urt_ficha(request, id_urt=None):
    return render(request, 'urts/urt_ciclo_ficha.html')


#RELATÓRIOS
def urt_relatorio_ficha(request, urt_id=None):
    urt = URTs.objects.get(id=urt_id)
    tab_especies_vegetais = URTespecieVegetal.objects.filter(del_status=False, urt=urt_id)
    tab_especies_animais = URTespecieAnimal.objects.filter(del_status=False, urt=urt_id)
    tab_tecnicos = TecnicoURT.objects.filter(del_status=False, urt=urt_id)
    
    #Log Relatório
    usuario_nome = request.user.usuario_relacionado.primeiro_ultimo_nome
    data_hora_atual = datetime.now()
    data_hora = data_hora_atual.strftime('%d/%m/%Y %H:%M:%S')
    
    conteudo = {
        'urt': urt,
        'usuario': usuario_nome,
        'data_hora': data_hora,
        'tab_especies_vegetais': tab_especies_vegetais,
        'tab_especies_animais': tab_especies_animais,
    }
    return render(request, 'urts/urt_ficha_relatorio.html', conteudo)

