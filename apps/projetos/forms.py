from django import forms
from django_select2.forms import Select2Widget
from apps.usuarios.models import Usuarios
from apps.projetos.models import Projetos, ProjetosAtividadesProdutivas
from setup.choices import LISTA_UFS_SIGLAS, STATUS_PROJETO, SUBPROGRAMA, LISTA_ANOS, ATIVIDADES_ATEG

class FiltroProjetosForm(forms.Form):
    regional = forms.ChoiceField(
        choices=LISTA_UFS_SIGLAS,
        widget=forms.Select(attrs={
            'class': 'form-select',
            'id': 'filtro_regional',
            'style': 'width: 100px'
        }),
        label='Regional',
        required=False,
        initial='',
    )
    status = forms.ChoiceField(
        choices=STATUS_PROJETO,
        widget=forms.Select(attrs={
            'class': 'form-select',
            'id': 'filtro_status'
        }),
        label='Status',
        required=False,
        initial='',
    )
    subprograma = forms.ChoiceField(
        choices=SUBPROGRAMA,
        widget=forms.Select(attrs={
            'class': 'form-select',
            'id': 'filtro_subprograma',
            'style': 'width: 200px'
        }),
        label='Subprograma',
        required=False,
        initial='',
    )
    data_inicio = forms.DateField(
        widget=forms.DateInput(attrs={
            'class': 'form-control', 
            'type': 'date',
            'id': 'filtro_data_inicio'
        }),
        label='Data Início*',
        required=True
    )
    data_fim = forms.DateField(
        widget=forms.DateInput(attrs={
            'class': 'form-control', 
            'type': 'date',
            'id': 'filtro_data_fim'
        }),
        label='Data Fim*',
        required=True
    )
    nome_plano_trabalho = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'filtro_nome_plano_trabalho'
        }),
        label='Plano de Trabalho*',
        required=True
    )

class ProjetosForm(forms.ModelForm):
    id_projeto_sisateg = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'id_projeto_sisateg'
        }),
        max_length=40,
        label='ID Projeto SisATeG*',
        required=True
    )
    regional = forms.ChoiceField(
        choices=LISTA_UFS_SIGLAS,
        widget=forms.Select(attrs={
            'class': 'form-select',
            'id': 'id_regional'
        }),
        label='Regional*',
        required=True
    )
    status = forms.ChoiceField(
        choices=STATUS_PROJETO,
        widget=forms.Select(attrs={
            'class': 'form-select',
            'id': 'id_status'
        }),
        label='Status Projeto*',
        required=True
    )
    nome_plano_trabalho = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'id_nome_plano_trabalho'
        }),
        label='Nome do Plano de Trabalho*',
        required=True
    )
    n_processo = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'id_n_processo',
        }),
        label='Nº do Processo*',
        required=False
    )
    termo_adesao = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'id_termo_adesao'
        }),
        label='Termo de Adesão',
        required=False
    )
    n_plano_trabalho = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'id_n_plano_trabalho'
        }),
        label='Nº do Plano de Trabalho',
        required=False
    )
    n_reformulacoes = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'id': 'id_n_reformulacoes'
        }),
        label='Nº de Reformulações',
        required=False
    )
    n_docs = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'id_n_docs'
        }),
        label='Nº DOCs',
        required=False
    )
    n_aviso_encerramento = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'id_aviso_encerramento'
        }),
        label='Nº Aviso Encerramento',
        required=False
    )
    n_prestacao_contas = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'id_n_prestacao_contas'
        }),
        label='Nº Prestação de Contas',
        required=False
    )
    subprograma = forms.ChoiceField(
        choices=SUBPROGRAMA,
        widget=forms.Select(attrs={
            'class': 'form-select',
            'id': 'id_subprograma',
            'style': 'width: 200px'
        }),
        label='Subprograma*',
        required=True
    )
    geracao_projeto = forms.ChoiceField(
        choices=LISTA_ANOS,
        widget=forms.Select(attrs={
            'class': 'form-select',
            'id': 'id_geracao_projeto'
        }),
        label='Geração*',
        required=True
    )
    gestor_dateg = forms.ModelChoiceField(
        queryset=Usuarios.objects.all(),
        widget=Select2Widget(attrs={
            'class': 'form-select',
            'id': 'id_gestor_dateg',
        }),
        label='Gestor DATeG*',
        required=True,
    )
    data_inicio = forms.DateField(
        widget=forms.DateInput(attrs={
            'class': 'form-control', 
            'type': 'date',
            'id': 'id_data_inicio'
        }),
        label='Data Início*',
        required=True
    )
    data_fim = forms.DateField(
        widget=forms.DateInput(attrs={
            'class': 'form-control', 
            'type': 'date',
            'id': 'id_data_fim'
        }),
        label='Data Fim*',
        required=True
    )
    n_tecnicos = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'id': 'id_n_tecnicos'
        }),
        label='Técnicos',
        required=False
    )
    n_supervisores = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'id': 'id_n_supervisores'
        }),
        label='Supervisores',
        required=False
    )
    n_tecnicos_supervisores_ead = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'id': 'id_n_tecnicos_supervisores_ead'
        }),
        label='Supervisores e Técnicos EAD',
        required=False
    )
    observacoes_gerais = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'id': 'id_observacoes_gerais'
        }),
        label='Observações Gerais',
        required=False
    )
    

    class Meta:
        model = Projetos
        exclude = ['usuario_registro', 'usuario_atualizacao', 'registro_data', 'ult_atual_data', 'log_n_edicoes', 'del_status', 'del_data', 'del_usuario']
        # Inclua ou exclua campos conforme necessário

    def save(self, commit=True, *args, **kwargs):
        projeto = super().save(commit=False, *args, **kwargs)
        # Aqui você pode adicionar lógica adicional antes de salvar o projeto
        if commit:
            projeto.save()
        return projeto


class ProjetosAtividadesForm(forms.ModelForm):
    atividade = forms.ChoiceField(
        choices=ATIVIDADES_ATEG,
        widget=forms.Select(attrs={
            'class': 'form-select',
            'id': 'id_atividade'
        }),
        label='Atividade Produtiva',
        required=True
    )
    n_propriedades = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'id': 'id_n_propriedades',
            'style': 'text-align: right'
        }),
        label='Nº de Propriedades',
        required=True,
    )
    n_cadernos = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'id': 'id_n_cadernos',
            'style': 'text-align: right'
        }),
        label='Nº de Cadernos',
        required=True,
    )
    n_tecnicos = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'id': 'id_n_tecnicos',
            'style': 'text-align: right'
        }),
        label='Nº de Técnicos',
        required=True,
    )
    n_supervisores = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'id': 'id_n_supervisores',
            'style': 'text-align: right'
        }),
        label='Nº de Supervisores',
        required=True,
    )
    n_tecnicos_supervisores_ead = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'id': 'id_n_supervisores_tecnicos_ead',
            'style': 'text-align: right'
        }),
        label='Nº de Superv./Téc. EAD',
        required=True,
    )
    projeto = forms.ModelChoiceField(
        queryset=Projetos.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-select',
            'id': 'id_projeto',
        }),
        label='Projeto',
        required=True,
    )
    observacoes_gerais = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'id': 'id_observacoes_gerais',
            'style': 'min-height: 90px;'
        }),
        label='Observações Gerais',
        required=False
    )
    
    class Meta:
        model = ProjetosAtividadesProdutivas
        exclude = ['usuario_registro', 'usuario_atualizacao', 'registro_data', 'ult_atual_data', 'log_n_edicoes', 'del_status', 'del_data', 'del_usuario']

    def save(self, commit=True, *args, **kwargs):
        projeto_atividade_produtiva = super().save(commit=False, *args, **kwargs)

        campos_numericos = [
            'n_propriedades', 'n_cadernos', 'n_tecnicos',
            'n_supervisores', 'n_tecnicos_supervisores_ead'
        ]
        for campo in campos_numericos:
            valor = getattr(projeto_atividade_produtiva, campo)
            if valor is None or valor == '':
                setattr(projeto_atividade_produtiva, campo, 0)

        #Observações gerais
        observacoes = getattr(projeto_atividade_produtiva, 'observacoes_gerais', '')
        if observacoes == '':
            setattr(projeto_atividade_produtiva, 'observacoes_gerais', 'Sem observações.')

        if commit:
            projeto_atividade_produtiva.save()
        return projeto_atividade_produtiva