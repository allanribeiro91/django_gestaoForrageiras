from django import forms
from apps.produtos.models import DenominacoesGenericas, ProdutosFarmaceuticos
from setup.choices import TIPO_PRODUTO, FORMA_FARMACEUTICA, STATUS_INCORPORACAO, CONCENTRACAO_TIPO

class DenominacoesGenericasForm(forms.ModelForm):    
    denominacao = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    tipo_produto = forms.ChoiceField(choices=TIPO_PRODUTO, required=True, widget=forms.Select(attrs={'class':'form-control'}))
    
    class Meta:
        model = DenominacoesGenericas
        exclude = ['usuario_registro', 'usuario_atualizacao', 'log_n_edicoes', 'del_status', 'del_data', 'del_usuario']
        labels = {
            'denominacao': 'Denominação Genérica',
            'tipo_produto': 'Tipo de Produto',
            'unidade_basico': 'Básico',
            'unidade_especializado': 'Especializado',
            'unidade_estrategico': 'Estratégico',
            'unidade_farm_popular': 'Farmácia Popular',
            'hospitalar': 'Hospitalar',
            'observacoes_gerais': 'Observações',
        }
        widgets = {
            'unidade_basico': forms.CheckboxInput(attrs={'class':'form-control'}),
            'unidade_especializado': forms.CheckboxInput(attrs={'class':'form-control'}),
            'unidade_estrategico': forms.CheckboxInput(attrs={'class':'form-control'}),
            'unidade_farm_popular': forms.CheckboxInput(attrs={'class':'form-control'}),
            'hospitalar': forms.CheckboxInput(attrs={'class':'form-control'}),
            'observacoes_gerais': forms.Textarea(attrs={'class':'form-control'}),
        }

class ProdutosFarmaceuticosForm(forms.ModelForm):    
    
    class Meta:
        model = ProdutosFarmaceuticos
        exclude = ['usuario_registro', 'usuario_atualizacao', 'log_n_edicoes', 'del_status', 'del_data', 'del_usuario']
        labels = {
            'denominacao': 'Denominação',
            'produto': 'Produto',
            'concentracao_tipo': 'Tipo de Concentração',
            'concentracao': 'Concentração',
            'forma_farmaceutica': 'Forma Farmacêutica',
            'oncologico': 'Oncológico',
            'biologico': 'Biológico',
            'aware': 'AWaRe',
            'atc': 'Código ATC',
            'atc_descricao': 'ATC',
            'incorp_status': 'Status Incorporação',
            'incorp_data': 'Data de Incorporação',
            'incorp_portaria': 'Portaria de Incorporação',
            'incorp_link': 'Link de Incorporação',
            'exclusao_data': 'Data de Exclusão',
            'exclusao_portaria': 'Portaria de Exclusão',
            'exclusao_link': 'Link de Exclusão',
            'comp_basico': 'Básico',
            'comp_especializado': 'Especializado',
            'comp_estrategico': 'Estratégico',
            'comp_basico_programa': 'Programa - Básico',
            'comp_especializado_grupo': 'Grupo AF - Especializado',
            'comp_estrategico_programa': 'Programa - Estratégico',
            'sigtap_possui': 'Possui SIGTAP',
            'sigtap_codigo': 'Código SIGTAP',
            'sigtap_nome': 'Nome SIGTAP',
            'sismat_possui': 'Possui SISMAT',
            'sismat_codigo': 'Código SISMAT',
            'sismat_nome': 'Nome SISMAT',
            'catmat_possui': 'Possui CATMAT',
            'catmat_codigo': 'Código CATMAT',
            'catmat_nome': 'Nome CATMAT',
            'obm_possui': 'Possui OBM',
            'obm_codigo': 'Código OBM',
            'obm_nome': 'Nome OBM',
            'observacoes_gerais': 'Observações Gerais',
        }
        widgets = {
            'denominacao': forms.TextInput(attrs={'class':'form-control'}),   
            'produto': forms.TextInput(attrs={'class':'form-control'}),
            'concentracao_tipo': forms.Select(attrs={'class':'form-control'}),
            'concentracao': forms.TextInput(attrs={'class':'form-control'}),
            'forma_farmaceutica': forms.Select(attrs={'class':'form-control'}),
            'oncologico': forms.Select(attrs={'class':'form-select'}),
            'biologico': forms.Select(attrs={'class':'form-select'}),
            'aware': forms.Select(attrs={'class':'form-control'}),
            'atc': forms.Select(attrs={'class':'form-control'}),
            'atc_codigo': forms.TextInput(attrs={'class':'form-control'}),
            'incorp_status': forms.Select(attrs={'class':'form-control'}),
            'incorp_data': forms.DateInput(
                format='%d/%m/%Y',
                attrs={
                    'type': 'date',
                    'class':'form-control'}),
            'incorp_portaria': forms.TextInput(attrs={'class':'form-control'}),
            'incorp_link': forms.URLInput(attrs={'class':'form-control'}),
            'exclusao_data': forms.DateInput(
                format='%d/%m/%Y',
                attrs={
                    'type': 'date',
                    'class':'form-control'}),
            'exclusao_portaria': forms.TextInput(attrs={'class':'form-control'}),
            'exclusao_link': forms.URLInput(attrs={'class':'form-control'}),
            'comp_basico': forms.CheckboxInput(attrs={'class':'form-control'}),
            'comp_especializado': forms.CheckboxInput(attrs={'class':'form-control'}),
            'comp_estrategico': forms.CheckboxInput(attrs={'class':'form-control'}),
            'disp_farmacia_popular': forms.CheckboxInput(attrs={'class':'form-control'}),
            'hospitalar': forms.CheckboxInput(attrs={'class':'form-control'}),
            'sigtap_possui': forms.CheckboxInput(attrs={'class':'form-control'}),
            'sigtap_codigo': forms.TextInput(attrs={'class':'form-control'}),
            'sigtap_nome': forms.TextInput(attrs={'class':'form-control'}),
            'sismat_possui': forms.CheckboxInput(attrs={'class':'form-control'}),
            'sismat_codigo': forms.TextInput(attrs={'class':'form-control'}),
            'sismat_nome': forms.TextInput(attrs={'class':'form-control'}),
            'catmat_possui': forms.CheckboxInput(attrs={'class':'form-control'}),
            'catmat_codigo': forms.TextInput(attrs={'class':'form-control'}),
            'catmat_nome': forms.TextInput(attrs={'class':'form-control'}),
            'obm_possui': forms.CheckboxInput(attrs={'class':'form-control'}),
            'obm_codigo': forms.TextInput(attrs={'class':'form-control'}),
            'obm_nome': forms.TextInput(attrs={'class':'form-control'}),
            'observacoes_gerais': forms.Textarea(attrs={'class':'form-control'}),
        }

