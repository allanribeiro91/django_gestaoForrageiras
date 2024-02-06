from django import forms
from apps.usuarios.models import Usuarios
from apps.fornecedores.models import Fornecedores, Fornecedores_Faq, Fornecedores_Representantes, Fornecedores_Comunicacoes
from setup.choices import UNIDADE_DAF2, CNPJ_HIERARQUIA, CNPJ_PORTE, TIPO_DIREITO, FAQ_FORNECEDOR_TOPICO, CARGOS_FUNCOES, GENERO_SEXUAL, TIPO_COMUNICACAO, STATUS_ENVIO_COMUNICACAO

class FornecedoresForm(forms.ModelForm):    
    cnpj = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    hierarquia = forms.ChoiceField(required=False, choices=CNPJ_HIERARQUIA, widget=forms.Select(attrs={'class':'form-control'}))
    porte = forms.ChoiceField(choices=CNPJ_PORTE, required=True, widget=forms.Select(attrs={'class':'form-control'}))
    tipo_direito = forms.ChoiceField(choices=TIPO_DIREITO, widget=forms.Select(attrs={'class':'form-control'}))
    data_abertura = forms.DateField(required=False, widget=forms.DateInput(attrs={'type':'date', 'class':'form-control'}))
    natjuridica_codigo = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    natjuridica_descricao = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    razao_social = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    nome_fantasia = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    ativ_principal_cod = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    ativ_principal_descricao = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    end_cep = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    end_uf = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    end_municipio = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    end_logradouro = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    end_numero = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    end_bairro = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    observacoes_gerais = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control'}))
    
    class Meta:
        model = Fornecedores
        exclude = ['usuario_registro', 'usuario_atualizacao', 'log_n_edicoes', 'del_status', 'del_data', 'del_usuario']
        labels = {
            'cnpj': 'CNPJ',
            'hierarquia': 'Hierarquia',
            'porte': 'Porte',
            'tipo_direito': 'Tipo de Direito',
            'data_abertura': 'Data de Abertura',
            'natjuridica_codigo': 'Cód. Nat. Jurídica',
            'natjuridica_descricao': 'Natureza Jurídica',
            'razao_social': 'Razão Social',
            'nome_fantasia': 'Nome Fantasia',
            'ativ_principal_cod': 'Cód. Ativ. Principal',
            'ativ_principal_descricao': 'Atividade Principal',
            'end_cep': 'CEP',
            'end_uf': 'UF',
            'end_municipio': 'Município',
            'end_logradouro': 'Logradouro',
            'end_numero': 'Número',
            'end_bairro': 'Bairro',
            'observacoes_gerais': 'Observações gerais',
        }
    
    def clean_observacoes_gerais(self):
        observacoes = self.cleaned_data.get('observacoes_gerais')
        
        if not observacoes:
            return "Sem observações."
        
        return observacoes

class FornecedoresFaqForm(forms.ModelForm):
    topico = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    topico_outro = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    contexto = forms.CharField(required=True, widget=forms.Textarea(attrs={'class':'form-control'}))
    resposta = forms.CharField(required=True, widget=forms.Textarea(attrs={'class':'form-control'}))
    
    #observações gerais
    observacoes_gerais = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control'}))

    class Meta:
        model = Fornecedores_Faq
        exclude = ['usuario_registro', 'usuario_atualizacao', 'log_n_edicoes', 'del_status', 'del_data', 'del_usuario']
        labels = {
            'topico': 'Tópico',
            'topico_outro': 'Hierarquia',
            'contexto': 'Porte',
            'resposta': 'Tipo de Direito',
            'observacoes_gerais': 'Observações gerais',
        }

    def clean_observacoes_gerais(self):
        observacoes = self.cleaned_data.get('observacoes_gerais')
        
        if not observacoes:
            return "Sem observações."
        
        return observacoes


class FornecedoresRepresentantesForm(forms.ModelForm):
    fornecedor = forms.ModelChoiceField(
        queryset=Fornecedores.objects.all(), 
        required=True, 
    )
    cpf = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    nome_completo = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    data_nascimento = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        label='Data de Nascimento'
    )
    genero_sexual = forms.ChoiceField(
        required=False,
        choices=GENERO_SEXUAL,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    cargo = forms.ChoiceField(
        required=False,
        choices=CARGOS_FUNCOES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    cargo_outro = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    telefone = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    celular = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        required=False,
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    linkedin = forms.URLField(
        required=False,
        widget=forms.URLInput(attrs={'class': 'form-control'})
    )
    observacoes_gerais = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control'}),
        label='Observações Gerais'
    )

    class Meta:
        model = Fornecedores_Representantes
        exclude = ['usuario_registro', 'usuario_atualizacao', 'log_n_edicoes', 'del_status', 'del_data', 'del_usuario']

    def clean_observacoes_gerais(self):
        observacoes = self.cleaned_data.get('observacoes_gerais')
        return observacoes or "Sem observações."


class FornecedoresComunicacoesForm(forms.ModelForm):
    unidade_daf = forms.ChoiceField(
        choices=UNIDADE_DAF2,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Unidade DAF'
    )
    tipo_comunicacao = forms.ChoiceField(
        choices=TIPO_COMUNICACAO,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Tipo de Comunicação'
    )
    topico_comunicacao = forms.ChoiceField(
        choices=FAQ_FORNECEDOR_TOPICO,
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=False,
        label='Tópico de Comunicação'
    )
    assunto = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False,
        label='Assunto'
    )
    demanda_original = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'}),
        required=False,
        label='Demanda Original'
    )
    destinatario = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'}),
        required=False,
        label='Destinatário'
    )
    mensagem_encaminhada = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'}),
        required=False,
        label='Mensagem Encaminhada'
    )
    status_envio = forms.ChoiceField(
        choices=STATUS_ENVIO_COMUNICACAO,
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=False,
        label='Status do Envio'
    )
    data_envio = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        required=False,
        label='Data de Envio'
    )
    responsavel_resposta = forms.ModelChoiceField(
        queryset=Usuarios.objects.all(), 
        required=False, 
        widget=forms.Select(attrs={'class':'form-control'})
    )
    outro_responsavel = forms.CharField(
        max_length=80,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False,
        label='Outro Responsável'
    )
    observacoes_gerais = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'}),
        required=False,
        label='Observações Gerais'
    )

    class Meta:
        model = Fornecedores_Comunicacoes
        exclude = ['usuario_registro', 'usuario_atualizacao', 'log_n_edicoes', 'del_status', 'del_data', 'del_usuario']

    def __init__(self, *args, **kwargs):
        super(FornecedoresComunicacoesForm, self).__init__(*args, **kwargs)
        # Adiciona uma opção vazia no início do dropdown
        self.fields['responsavel_resposta'].choices = [(None, 'Nenhum')] + list(self.fields['responsavel_resposta'].choices) + [('outro', 'Outro')]

    def clean_observacoes_gerais(self):
        observacoes = self.cleaned_data.get('observacoes_gerais')
        return observacoes or "Sem observações."