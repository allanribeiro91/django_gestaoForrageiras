from django import forms
from django.core.exceptions import ValidationError
from apps.usuarios.models import Usuarios
from apps.produtos.models import DenominacoesGenericas
from apps.processos_aquisitivos.models import ProaqDadosGerais, ProaqEvolucao, ProaqTramitacao
from setup.choices import STATUS_PROAQ, UNIDADE_DAF2, STATUS_FASE

class DenominacaoModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.get_denominacao_nome()

class ProaqDadosGeraisForm(forms.ModelForm):    
    unidade_daf = forms.ChoiceField(choices=UNIDADE_DAF2, required=True, widget=forms.Select(attrs={'class':'form-control'}))
    modalidade_aquisicao = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    numero_processo_sei = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    numero_etp = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    status = forms.ChoiceField(choices=STATUS_PROAQ, required=True, widget=forms.Select(attrs={'class':'form-control'}))
    responsavel_tecnico = forms.ModelChoiceField(queryset=Usuarios.objects.all(), required=True, widget=forms.Select(attrs={'class':'form-control'}))
    observacoes_gerais = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control'}))
    denominacao = DenominacaoModelChoiceField(
        queryset=DenominacoesGenericas.objects.filter(del_status=False),
        required=True,
        widget=forms.Select(attrs={'class':'form-control'}),
        empty_label="Não Informado"
    )
    
    class Meta:
        model = ProaqDadosGerais
        exclude = ['usuario_registro', 'usuario_atualizacao', 'log_n_edicoes', 'del_status', 'del_data', 'del_usuario']
        labels = {
            'unidade_daf': 'Unidade DAF',
            'modalidade_aquisicao': 'Modalidade de Aquisição',
            'numero_processo_sei': 'Processo SEI',
            'numero_etp': 'Número do ETP',
            'status': 'Status',
            'responsavel_tecnico': 'Responsável Técnico',
            'denominacao': 'Denominação Genérica',
            'observacoes_gerais': 'Observações',
        }


class ProaqEvolucaoForm(forms.ModelForm):
    proaq = forms.ModelChoiceField(
        queryset=ProaqDadosGerais.objects.all(), 
        required=True, 
        widget=forms.Select(attrs={'class':'form-control'}),
        label='Proaq'
    )
    fase = forms.IntegerField(
        required=True, 
        widget=forms.NumberInput(attrs={'class':'form-control'}),
        label='Fase'
    )
    status = forms.ChoiceField(
        choices=STATUS_FASE, 
        required=True, 
        widget=forms.Select(attrs={'class':'form-control'}),
        label='Status'
    )
    data_inicio = forms.DateField(
        required=False, 
        widget=forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
        label='Data de Início'
    )
    data_fim = forms.DateField(
        required=False, 
        widget=forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
        label='Data Fim'
    )
    comentario = forms.CharField(
        required=False, 
        widget=forms.Textarea(attrs={'class':'form-control'}),
        label='Comentário'
    )
    
    class Meta:
        model = ProaqEvolucao
        exclude = ['usuario_registro', 'usuario_atualizacao', 'log_n_edicoes', 'del_status', 'del_data', 'del_usuario',]
        labels = {
            'proaq': 'proaq',
            'fase': 'Fase',
            'status': 'Status',
            'data_inicio': 'Data de Início',
            'data_fim': 'Data Fim',
            'comentario': 'Comentário',
        }
    
    def clean(self):
        cleaned_data = super().clean()
        data_inicio = cleaned_data.get("data_inicio")
        data_fim = cleaned_data.get("data_fim")
        comentario = cleaned_data.get("comentario")
        
        #Validação de data
        if data_inicio and data_fim and data_inicio > data_fim:
            raise ValidationError("A data de início não pode ser posterior à data de fim.")
        
        # Ajuste para o campo comentario
        if comentario in [None, '']:
            cleaned_data['comentario'] = "Sem comentários."
        
        return cleaned_data


class ProaqTramitacaoForm(forms.ModelForm):
    proaq = forms.ModelChoiceField(
        queryset=ProaqDadosGerais.objects.all(), 
        required=True, 
        widget=forms.Select(attrs={'class':'form-control'}),
        label='Proaq'
    )
    documento_sei = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control'}),
        label='Documento SEI',
        max_length=20,
    )
    setor = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control'}),
        label='Setor',
        max_length=50,
    )
    etapa_processo = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control'}),
        label='Etapa do Processo',
        max_length=100,
    )
    data_entrada = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'class':'form-control'}),
        label='Data de Entrada'
    )
    previsao_saida = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'class':'form-control'}),
        label='Previsão de Saída'
    )
    data_saida = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'class':'form-control'}),
        label='Data de Saída'
    )
    observacoes = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'class':'form-control'}),
        label='Observações'
    )

    class Meta:
        model = ProaqTramitacao
        exclude = ['usuario_registro', 'usuario_atualizacao', 'log_n_edicoes', 'del_status', 'del_data', 'del_usuario',]
        labels = {
            'usuario_registro': 'Usuário Registro',
            'usuario_atualizacao': 'Usuário Atualização',
            'proaq': 'ID PROAQ',
            'documento_sei': 'Documento SEI',
            'setor': 'Setor',
            'etapa_processo': 'Etapa do Processo',
            'data_entrada': 'Data de Entrada',
            'previsao_saida': 'Previsão de Saída',
            'data_saida': 'Data de Saída',
            'observacoes': 'Observações',
            'del_usuario': 'Usuário Deletado',
        }