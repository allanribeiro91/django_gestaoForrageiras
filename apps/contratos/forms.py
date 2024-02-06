from django import forms
from django_select2.forms import Select2Widget
from apps.usuarios.models import Usuarios
from apps.produtos.models import DenominacoesGenericas, ProdutosFarmaceuticos
from apps.fornecedores.models import Fornecedores
from apps.contratos.models import ContratosArps, ContratosArpsItens
from apps.contratos.models import Contratos
from setup.choices import STATUS_ARP, UNIDADE_DAF, TIPO_COTA, YES_NO, MODALIDADE_AQUISICAO, STATUS_FASE, LEI_LICITACAO

UNIDADE_DAF = [item for item in UNIDADE_DAF if item[0] not in ['cofisc', 'gabinete']]

class ContratosArpsForm(forms.ModelForm):
    unidade_daf = forms.ChoiceField(
        choices=UNIDADE_DAF,
        widget=forms.Select(attrs={
            'class': 'form-select',
            'id': 'arp_unidade_daf',
        }),
        label='Unidade DAF',
        initial='',
        required=True,
    )
    lei_licitacao = forms.ChoiceField(
        choices=LEI_LICITACAO,
        widget=forms.Select(attrs={
            'class': 'form-select',
            'id':'arp_lei_licitacao'
        }),
        label='Lei de Licitação',
        initial='nao_informado',
        required=True,
    )
    numero_processo_sei = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'id': 'arp_processo_sei', 
            'name': 'numero_processo_sei',
            'style': 'width: 180px !important;'
        }),
        label='Nº Processo SEI',
        required=True,
    )
    numero_documento_sei = forms.CharField(
        max_length=10,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'arp_documento_sei',
            'style': 'width: 180px !important;'
        }),
        label='Documento SEI',
        required=True,
    )
    numero_arp = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'arp_numero_arp',
            'style': 'width: 180px !important;'
        }),
        label='Nº da ARP',
        required=True,
    )
    status = forms.ChoiceField(
        choices=STATUS_ARP,
        widget=forms.Select(attrs={
            'class': 'form-select',
            'id':'arp_status'
        }),
        label='Status',
        initial='',
        required=True,
    )
    data_publicacao = forms.DateField(
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date',
        }),
        required=False,
        label='Data Publicação'
    )
    denominacao = forms.ModelChoiceField(
        queryset=DenominacoesGenericas.objects.all().order_by('denominacao'),
        widget=Select2Widget(attrs={
            'class': 'form-select', 
            'id': 'arp_denominacao',
            'disabled': True, 
        }),
        label='Denominação Genérica',
        empty_label='Selecione uma denominação genérica',
        required=False,
    )
    fornecedor = forms.ModelChoiceField(
        queryset=Fornecedores.objects.all().order_by('nome_fantasia'),
        widget=Select2Widget(attrs={
            'class': 'form-select', 
            'id': 'cnpj_fornecedor', 
        }),
        label='Fornecedor',
        empty_label='Selecione um CNPJ',
        required=False,
    )
    observacoes_gerais = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control auto-expand',
            'rows': 1,
            'style': 'padding-top: 10px; height: 120px;',
            }),
        required=False,
        label='Observações Gerais'
    )

    class Meta:
        model = ContratosArps
        exclude = ['usuario_registro', 'usuario_atualizacao', 'log_n_edicoes', 'del_status', 'del_data', 'del_usuario']

    def clean_observacoes_gerais(self):
        observacoes = self.cleaned_data.get('observacoes_gerais')
        return observacoes or "Sem observações."


class ContratosArpsItensForm(forms.ModelForm):
    arp = forms.ModelChoiceField(
        queryset=ContratosArps.objects.all(),
        widget=Select2Widget(attrs={
            'class': 'form-select',
            'id': 'arp',
        }),
        label='ARP',
        required=True,
    )
    numero_item = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'id': 'arp_n_item',
            'style': 'width: 100px'
        }),
        label='Nº do Item',
        min_value=1,
        max_value=20,
        required=True,
    )
    tipo_cota = forms.ChoiceField(
        choices=[('', '')] + TIPO_COTA,
        widget=forms.Select(attrs={
            'class': 'form-select',
            'id': 'arp_tipo_cota',
            'style': 'width: 150px'
        }),
        label='Tipo de Cota',
        initial='',
        required=True,
    )
    empate_ficto = forms.ChoiceField(
        choices=[('', '')] + YES_NO,
        widget=forms.Select(attrs={
            'class': 'form-select',
            'id': 'arp_empate_ficto',
            'style': 'width: 150px',
        }),
        label='Empate Ficto',
        initial='',
        required=True,
    )
    produto = forms.ModelChoiceField(
        queryset=ProdutosFarmaceuticos.objects.all(),
        widget=Select2Widget(attrs={
            'class': 'form-select',
            'id': 'arp_produto_farmaceutico',
        }),
        label='Produto Farmacêutico',
        required=True,
    )
    valor_unit_homologado = forms.FloatField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'arp_valor_unitario',
            'style': 'text-align: right'
        }),
        label='Valor Unit. Homologado',
        required=True,
    )
    valor_unit_reequilibrio_bool = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input',
            'id': 'arp_valor_reequilibrio_check',
        }),
        label='Reequilíbrio de Valor Unitário',
        required=False,
    )
    valor_unit_reequilibrio = forms.FloatField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'arp_valor_reequilibrio',
            'style': 'text-align: right',
            'readonly': 'true'
        }),
        label='Valor Unit. Reequilíbrio',
        required=False,
    )
    qtd_registrada = forms.FloatField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'arp_qtd_registrada',
            'style': 'text-align: right',
        }),
        label='Quantidade Registrada',
        required=False,
    )
    observacoes_gerais = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control auto-expand',
            'rows': 1,
            'style': 'padding-top: 10px; height: 80px;',
            'id': 'arp_observacoes_gerais'
            }),
        required=False,
        label='Observações Gerais'
    )

    class Meta:
        model = ContratosArpsItens
        exclude = ['usuario_registro', 'usuario_atualizacao', 'log_n_edicoes', 'del_status', 'del_data', 'del_usuario']

    def clean_observacoes_gerais(self):
        observacoes = self.cleaned_data.get('observacoes_gerais')
        return observacoes or "Sem observações."


class ContratosForm(forms.ModelForm):
    unidade_daf = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'ct_unidade_daf',
            'name': 'unidade_daf',
            'readonly': 'readonly',
            'style': 'width: 150px',
            'type': 'hidden',
        }),
        label='Unidade DAF',
        initial='',
        required=True,
    )
    lei_licitacao = forms.ChoiceField(
        choices=LEI_LICITACAO,
        widget=forms.Select(attrs={
            'class': 'form-select',
            'id':'ct_lei_licitacao',
        }),
        label='Lei de Licitação',
        initial='nao_informado',
        required=True,
    )
    modalidade_aquisicao = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'ct_modalidade_aquisicao',
            'readonly': 'readonly',
            'type': 'hidden',
        }),
        label='Modalidade de Aquisição',
        initial='',
    )
    numero_processo_sei = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'form-control full-width', 
            'id': 'ct_processo_sei', 
            'name': 'numero_processo_sei',
            
        }),
        label='Nº Processo SEI',
        required=True,
    )
    numero_documento_sei = forms.CharField(
        max_length=10,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'ct_documento_sei',
            'style': 'width: 150px !important;'
        }),
        label='Documento SEI',
        required=True,
    )
    numero_contrato = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'ct_numero_contrato',
            'name': 'numero_contrato',
            'style': 'width: 150px !important;'
        }),
        label='Nº do Contrato',
        required=True,
    )
    status = forms.ChoiceField(
        choices=STATUS_ARP,
        widget=forms.Select(attrs={
            'class': 'form-select',
            'id':'ct_status'
        }),
        label='Status',
        initial='',
        required=True,
    )
    data_publicacao = forms.DateField(
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date',
        }),
        required=False,
        label='Data Publicação'
    )
    arp = forms.ModelChoiceField(
        queryset=ContratosArps.objects.all(),
        widget=Select2Widget(attrs={
            'class': 'form-control',
            'id': 'ct_arp',
            'readonly': 'readonly',
            'type': 'hidden',
            'name': 'arp',
        }),
        label='Nº da ARP',
        initial='',
        required=False,
    )
    denominacao = forms.ModelChoiceField(
        queryset=DenominacoesGenericas.objects.all().order_by('denominacao'),
        widget=Select2Widget(attrs={
            'class': 'form-control',
            'id': 'ct_denominacao',
            'readonly': 'readonly',
            'type': 'hidden',
        }),
        label='Denominação Genérica',
        initial='',
    )
    fornecedor = forms.ModelChoiceField(
        queryset=Fornecedores.objects.all(),
        widget=Select2Widget(attrs={
            'class': 'form-control',
            'id': 'ct_fornecedor',
            'readonly': 'readonly',
            'type': 'hidden',
        }),
        label='Fornecedor',
        initial='',
    )
    observacoes_gerais = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control auto-expand',
            'rows': 1,
            'style': 'padding-top: 10px; height: 120px;',
            }),
        required=False,
        label='Observações Gerais'
    )

    class Meta:
        model = Contratos
        exclude = ['usuario_registro', 'usuario_atualizacao', 'log_n_edicoes', 'del_status', 'del_data', 'del_usuario']

    def clean_observacoes_gerais(self):
        observacoes = self.cleaned_data.get('observacoes_gerais')
        return observacoes or "Sem observações."