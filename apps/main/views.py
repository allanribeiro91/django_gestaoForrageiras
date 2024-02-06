from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from apps.main.forms import LoginForms, CadastroForms
from apps.usuarios.models import Usuarios
from apps.urts.models import URTs
from apps.main.models import UserAccessLog
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.contrib.auth.hashers import make_password
from django.db import transaction

def login(request):
    form = LoginForms(request.POST or None)
    
    if request.method == 'POST' and form.is_valid():
        cpf = form.cleaned_data['cpf']
        senha = form.cleaned_data['senha']

        usuario = auth.authenticate(request, username=cpf, password=senha)
        
        if not usuario:
            messages.error(request, "Usuário ou senha inválido!")
        else:
            usuario_validacao = usuario.usuario_relacionado
            
            #Verificações
            if not usuario_validacao.usuario_is_ativo:
                messages.error(request, "Usuário Inativado!")
            elif usuario_validacao.del_status:
                messages.error(request, "Usuário ou senha inválido!")
            elif not usuario_validacao.alocacao_ativa():
                messages.error(request, "Cadastro Em Análise!")
            else:
                # Todas as verificações passaram, então podemos logar o usuário
                auth.login(request, usuario)
                messages.info(request, f"{cpf} logado com sucesso!")
                
                # REGISTRAR O LOGIN
                log_entry = UserAccessLog(usuario=usuario.usuario_relacionado)
                log_entry.save()

                return redirect('home')
        
        # Se qualquer uma das verificações falhar, setar o valor inicial de 'cpf' e renderizar novamente
        form.fields['cpf'].initial = cpf
        return render(request, 'main/login.html', {'form': form})

    return render(request, 'main/login.html', {'form': form})

@login_required
def home(request):
    #usuário
    usuario = request.user.usuario_relacionado

    #alocação ativa do usuário
    alocacao_ativa = usuario.alocacao.filter(is_ativo=True).first()

    #totais
    tab_urts = URTs.objects.filter(del_status=False)
    tot_urts = tab_urts.count()
    tot_regionais = tab_urts.values_list('uf', flat=True).distinct().count()


    conteudo ={
        'usuario': usuario,
        'alocacao': alocacao_ativa,
        'tot_urts': tot_urts,
        'tot_regionais': tot_regionais,
    }
    return render(request, 'main/home.html', conteudo)

def logout(request):
    auth.logout(request)
    messages.info(request, "Logout efetuado com sucesso!")
    return redirect('login')

def cadastro(request):
    form = CadastroForms()

    if request.method == 'POST':
        form = CadastroForms(request.POST)

        #Validações
        if form.is_valid():
            senha_1 = form.cleaned_data["senha_1"]
            cpf = form.cleaned_data["cpf"]

            #Verificar se o CPF já está cadastrado na base
            erro = False
            if User.objects.filter(username=cpf).exists():
                messages.error(request, "CPF já cadastrado")
                erro = True
            
            if erro:
                return render(request, 'main/cadastro.html', {'form': form})
            
            #senha criptografada
            hashed_password = make_password(senha_1)

            #outros campos
            nome_usuario=form.cleaned_data["nome_usuario"]
            email_institucional=form.cleaned_data["email_institucional"]
            email_pessoal=form.cleaned_data["email_pessoal"]
            celular=form.cleaned_data["celular"]

            with transaction.atomic():
                #tabela auth_user
                auth_usuario = User.objects.create(
                    username=cpf,
                    email=email_pessoal,
                    password=hashed_password
                )

                #tabela main_usuario
                Usuarios.objects.create(
                    user=auth_usuario,
                    cpf=cpf,
                    nome_completo=nome_usuario,
                    celular=celular,
                    email_institucional=email_institucional,
                    email_pessoal=email_pessoal,
                )

            return redirect("cadastro_confirmacao")

    return render(request, 'main/cadastro.html', {'form': form})

def cadastro_confirmacao(request):
    return render(request, 'main/cadastro_confirmacao.html')