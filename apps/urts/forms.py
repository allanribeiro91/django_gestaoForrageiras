from django import forms
from django_select2.forms import Select2Widget
from apps.usuarios.models import Usuarios
from apps.urts.models import (URTs, URTespecieAnimal, URTespecieVegetal, 
                              TecnicoURT, Ciclo, CicloEspeciesVegetaisAnimais,
                              CicloAtividades)
from setup.choices import (LISTA_UFS_SIGLAS, LISTA_TEXTURA_SOLO, LISTA_MESES, 
                           ESPECIES_ANIMAIS, ESPECIES_VEGETAIS, LOCAL_PREPARO_AMOSTRAS,
                           STATUS_CONTRATOS_TECNICOS, FORMACAO_TECNICA,
                           CICLO_FASES, CICLO_STATUS_ATIVIDADE, CILCO_TIPO_ATIVIDADE,
                           PERIODO_CLIMATICO
                        )

#URT
class URTsForm(forms.ModelForm):
    #propriedade
    nome_propriedade = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'id_nome_propriedade'
        }),
        max_length=40,
        label='Nome da Propriedade',
        required=False
    )
    proprietario_nome = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'id_proprietario_nome'
        }),
        max_length=40,
        label='Proprietário',
        required=False
    )
    proprietario_telefone = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'id_proprietario_telefone'
        }),
        max_length=40,
        label='Telefone',
        required=False
    )
    proprietario_celular = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'id_proprietario_celular'
        }),
        max_length=40,
        label='Celular',
        required=False
    )
    proprietario_email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'id': 'id_proprietario_email'
        }),
        max_length=40,
        label='E-mail',
        required=False
    )
    #localizacao
    uf = forms.ChoiceField(
        choices=LISTA_UFS_SIGLAS,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'id_uf',
            'readonly': 'readonly',
            'style': 'text-transform: uppercase'
        }),
        label='UF',
        required=False
    )
    municipio = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'id_municipio',
            'readonly': 'readonly',
        }),
        max_length=120,
        label='Município',
        required=False,
    )
    endereco = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'id_endereco'
        }),
        max_length=240,
        label='Endereço',
        required=False
    )
    latlong = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'id_latlong'
        }),
        max_length=20,
        label='LatLong',
        required=False
    )
    pluscode = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'id_pluscode'
        }),
        max_length=20,
        label='PlusCode',
        required=False
    )
    #características gerais
    area_experimento = forms.IntegerField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'id_area_experimento',
            'style': 'text-align: right !important;'
        }),
        label='Área Experimento (ha)',
        required=False
    )
    textura_solo = forms.ChoiceField(
        choices=LISTA_TEXTURA_SOLO,
        widget=forms.Select(attrs={
            'class': 'form-select',
            'id': 'id_textura_solo'
        }),
        label='Textura do Solo',
        required=False
    )
    local_preparo_amostras = forms.ChoiceField(
        choices=LOCAL_PREPARO_AMOSTRAS,
        widget=forms.Select(attrs={
            'class': 'form-select',
            'id': 'id_local_preparo_amostras'
        }),
        label='Local Preparo Amostras',
        required=False
    )
    #clima
    precipitacao_anual = forms.IntegerField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'id_precipitacao_anual',
            'style': 'text-align: right !important;'
        }),
        label='Precipitação Anual (mm)',
        required=False
    )
    periodo_chuva_inicio = forms.ChoiceField(
        choices=LISTA_MESES,
        widget=forms.Select(attrs={
            'class': 'form-select',
            'id': 'id_periodo_chuva_inicio'
        }),
        label='Chuvoso - Início',
        required=False
    )
    periodo_chuva_fim = forms.ChoiceField(
        choices=LISTA_MESES,
        widget=forms.Select(attrs={
            'class': 'form-select',
            'id': 'id_periodo_chuva_fim'
        }),
        label='Chuvoso - Fim',
        required=False
    )
    periodo_seca_inicio = forms.ChoiceField(
        choices=LISTA_MESES,
        widget=forms.Select(attrs={
            'class': 'form-control',
            'id': 'id_periodo_seca_inicio',
            'readonly': 'readonly'
        }),
        label='Seca - Início',
        required=False,
    )
    periodo_seca_fim = forms.ChoiceField(
        choices=LISTA_MESES,
        widget=forms.Select(attrs={
            'class': 'form-control',
            'id': 'id_periodo_seca_fim',
            'readonly': 'readonly'
        }),
        label='Seca - Fim',
        required=False,
    )
    #dados da federacao
    federacao_presidente = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'id_federacao_presidente'
        }),
        max_length=120,
        label='Presidente da Federação',
        required=False
    )
    federacao_telefone = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'id_federacao_telefone'
        }),
        max_length=40,
        label='Telefone da Federação',
        required=False
    )
    federacao_email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'id': 'id_federacao_email'
        }),
        max_length=40,
        label='E-mail da Federação',
        required=False
    )
    #dados senar
    senar_superintendente = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'id_senar_superintendente'
        }),
        max_length=120,
        label='Superintendente do Senar',
        required=False
    )
    senar_telefone = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'id_senar_telefone'
        }),
        max_length=40,
        label='Telefone do Senar',
        required=False
    ) 
    senar_email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'id': 'id_senar_email'
        }),
        max_length=40,
        label='E-mail do Senar',
        required=False
    )
    #supervisor URT
    supervisor_nome = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'id_supervisor_nome'
        }),
        max_length=120,
        label='Supervisor da URT',
        required=False,
    )
    supervisor_telefone = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'id_supervisor_telefone'
        }),
        max_length=40,
        label='Telefone do Supervisor',
        required=False
    )  
    supervisor_email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'id': 'id_supervisor_email'
        }),
        max_length=40,
        label='E-mail do Supervisor',
        required=False
    )
    #observacoes
    observacoes_gerais = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control auto-expand',
            'rows': 1,
            'style': 'padding-top: 10px; height: 120px;',
            'id': 'id_observacoes_gerais'
            }),
        required=False,
        label='Observações Gerais'
    )

    class Meta:
        model = URTs
        exclude = ['usuario_registro', 'usuario_atualizacao', 'registro_data', 'ult_atual_data', 'log_n_edicoes', 'del_status', 'del_data', 'del_usuario']

    def save(self, commit=True, *args, **kwargs):
        especie_animal = super().save(commit=False, *args, **kwargs)
        if commit:
            especie_animal.save()
        return especie_animal


#Espécies Vegetais e Animais
class URTespecieVegetalForm(forms.ModelForm):
    especie_vegetal = forms.ChoiceField(
        choices=ESPECIES_VEGETAIS,
        widget=forms.Select(attrs={
            'class': 'form-select',
            'id': 'id_vegetal_especie_vegetal'
        }),
        label='Espécie Vegetal',
        required=True
    )
    variedades = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'id_vegetal_variedades'
        }),
        label='Variedades',
        required=True
    )
    area_utilizada = forms.FloatField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'id_vegetal_area_utilizada',
            'style': 'text-align: right !important;'
        }),
        label='Área Utilizada (ha)',
        required=True
    )
    producao_silagem = forms.NullBooleanField(
        widget=forms.NullBooleanSelect(attrs={
            'class': 'form-select',
            'id': 'id_vegetal_producao_silagem',
        }),
        label='Produção de Silagem',
        required=False,
    )
    urt = forms.ModelChoiceField(
        queryset=URTs.objects.all(),
        widget=Select2Widget(attrs={
            'class': 'form-select',
        }),
        label='URT',
        required=True,
    )
    observacoes_gerais = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control auto-expand',
            'rows': 1,
            'style': 'padding-top: 25px; height: 120px;',
            'id': 'id_vegetal_observacoes_gerais'
            }),
        required=False,
        label='Observações Gerais'
    )

    class Meta:
        model = URTespecieVegetal
        exclude = ['usuario_registro', 'usuario_atualizacao', 'registro_data', 'ult_atual_data', 'log_n_edicoes', 'del_status', 'del_data', 'del_usuario']

    def save(self, commit=True, *args, **kwargs):
        especie_vegetal = super().save(commit=False, *args, **kwargs)
        if commit:
            especie_vegetal.save()
        return especie_vegetal

class URTespecieAnimalForm(forms.ModelForm):
    especie_animal = forms.ChoiceField(
        choices=ESPECIES_ANIMAIS,
        widget=forms.Select(attrs={
            'class': 'form-select',
            'id': 'id_animal_especie_animal'
        }),
        label='Espécie Animal',
        required=True
    )
    racas = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'id_animal_racas'
        }),
        label='Raças',
        required=True
    )
    area_utilizada = forms.FloatField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'id_animal_area_utilizada',
            'style': 'text-align: right !important;'
        }),
        label='Área Utilizada (ha)',
        required=True
    )
    urt = forms.ModelChoiceField(
        queryset=URTs.objects.all(),
        widget=Select2Widget(attrs={
            'class': 'form-select',
            'id': 'id_animal_urt',
        }),
        label='URT',
        required=True,
    )
    observacoes_gerais = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control auto-expand',
            'rows': 1,
            'style': 'padding-top: 10px; height: 120px;',
            'id': 'id_animal_observacoes_gerais'
            }),
        required=False,
        label='Observações Gerais'
    )

    class Meta:
        model = URTespecieAnimal
        exclude = ['usuario_registro', 'usuario_atualizacao', 'registro_data', 'ult_atual_data', 'log_n_edicoes', 'del_status', 'del_data', 'del_usuario']

    def save(self, commit=True, *args, **kwargs):
        especie_animal = super().save(commit=False, *args, **kwargs)
        if commit:
            especie_animal.save()
        return especie_animal


#Técnicos das URTs
class TecnicoURTForm(forms.ModelForm):
    #dados do contrato
    status_contrato = forms.ChoiceField(
        choices=STATUS_CONTRATOS_TECNICOS,
        widget=forms.Select(attrs={
            'class': 'form-select',
            'id': 'id_tecnico_status_contrato'
        }),
        label='Status',
        initial='nao_informado',
        required=True
    )
    numero_contrato = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'id_tecnico_numero_contrato'
        }),
        label='Nº Contrato',
        required=False
    )
    data_inicio = forms.DateField(
        widget=forms.DateInput(attrs={
            'type':'date', 'class':'form-control'
        }),
        label='Data Início',
        required=False,
    )
    data_fim = forms.DateField(
        widget=forms.DateInput(attrs={
            'type':'date', 'class':'form-control'
        }),
        label='Data Fim',
        required=False,
    )
    #dados da empresa
    cnpj = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'id_tecnico_cnpj'
        }),
        label='CNPJ',
        required=False
    )
    razao_social = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'id_tecnico_razao_social'
        }),
        label='Razão Social',
        required=False
    )
    nome_fantasia = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'id_tecnico_nome_fantasia'
        }),
        label='Nome Fantasia',
        required=False
    )
    #dados do técnico
    cpf = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'id_tecnico_cpf'
        }),
        label='CPF',
        required=False
    )
    tecnico = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'id_tecnico_tecnico'
        }),
        label='Nome',
        required=True
    )
    formacao_tecnica = forms.ChoiceField(
        choices=FORMACAO_TECNICA,
        widget=forms.Select(attrs={
            'class': 'form-select',
            'id': 'id_tecnico_formacao_tecnica'
        }),
        label='Formação Técnica',
        initial='nao_informado',
        required=False
    )
    celular = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'id_tecnico_celular'
        }),
        max_length=15,
        label='Celular',
        required=False
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'id': 'id_tecnico_email'
        }),
        max_length=80,
        label='E-mail',
        required=False
    )
    urt = forms.ModelChoiceField(
        queryset=URTs.objects.all(),
        widget=Select2Widget(attrs={
            'class': 'form-select',
            'id': 'id_tecnico_urt',
        }),
        label='URT',
        required=True,
    )
    observacoes_gerais = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control auto-expand',
            'rows': 1,
            'style': 'padding-top: 30px; height: 120px;',
            'id': 'id_tecnico_observacoes_gerais'
            }),
        required=False,
        label='Observações Gerais'
    )

    class Meta:
        model = TecnicoURT
        exclude = ['usuario_registro', 'usuario_atualizacao', 'registro_data', 'ult_atual_data', 'log_n_edicoes', 'del_status', 'del_data', 'del_usuario']

    def save(self, commit=True, *args, **kwargs):
        tecnico_urt = super().save(commit=False, *args, **kwargs)
        if commit:
            tecnico_urt.save()
        return tecnico_urt


#Ciclos
class CicloForm(forms.ModelForm):
    numero_ciclo = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'id': 'id_ciclo'
        }),
        label='Ciclo',
        required=True
    )
    fase1_inicio = forms.DateField(
        widget=forms.DateInput(attrs={
            'class': 'form-control'
        })
    )
    fase1_fim = forms.DateField(
        widget=forms.DateInput(attrs={
            'class': 'form-control'
        })
    )
    fase2_inicio = forms.DateField(
        widget=forms.DateInput(attrs={
            'class': 'form-control'
        })
    )
    fase2_fim = forms.DateField(
        widget=forms.DateInput(attrs={
            'class': 'form-control'
        })
    )
    fase3_inicio = forms.DateField(
        widget=forms.DateInput(attrs={
            'class': 'form-control'
        })
    )
    fase3_fim = forms.DateField(
        widget=forms.DateInput(attrs={
            'class': 'form-control'
        })
    )
    urt = forms.ModelChoiceField(
        queryset=URTs.objects.all(),
        widget=Select2Widget(attrs={
            'class': 'form-select',
        }),
        label='URT',
        required=True,
    )
    observacoes_gerais = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control auto-expand',
            'rows': 1,
            'style': 'padding-top: 25px; height: 120px;',
            'id': 'ciclo_vegetal_observacoes_gerais'
            }),
        required=False,
        label='Observações Gerais'
    )

    class Meta:
        model = Ciclo
        exclude = ['usuario_registro', 'usuario_atualizacao', 'registro_data', 'ult_atual_data', 'log_n_edicoes', 'del_status', 'del_data', 'del_usuario']

    def save(self, commit=True, *args, **kwargs):
        ciclo = super().save(commit=False, *args, **kwargs)
        if commit:
            ciclo.save()
        return ciclo
    
class CicloEspeciesVegetaisAnimaisForm(forms.ModelForm):
    tipo_especie = forms.ChoiceField(
        choices=ESPECIES_VEGETAIS,
        widget=forms.Select(attrs={
            'class': 'form-select',
            'id': 'ciclo_tipo_especie'
        }),
        label='Tipo de Espécie',
        required=True
    )
    area_utilizada = forms.FloatField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'ciclo_especie_area_utilizada',
            'style': 'text-align: right !important;'
        }),
        label='Área Utilizada (ha)',
        required=False
    )
    #dados da espécie vegetal
    especie_vegetal = forms.ChoiceField(
        choices=ESPECIES_VEGETAIS,
        widget=forms.Select(attrs={
            'class': 'form-select',
            'id': 'ciclo_especie_vegetal'
        }),
        label='Espécie Vegetal',
        required=False
    )
    variedades = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'ciclo_especie_vegetal_variedades'
        }),
        label='Variedades',
        required=False
    )
    producao_silagem = forms.NullBooleanField(
        widget=forms.NullBooleanSelect(attrs={
            'class': 'form-select',
            'id': 'ciclo_especie_vegetal_producao_silagem',
        }),
        label='Produção de Silagem',
        required=False,
    )
    #dados da espécie animal
    especie_animal = forms.ChoiceField(
        choices=ESPECIES_ANIMAIS,
        widget=forms.Select(attrs={
            'class': 'form-select',
            'id': 'ciclo_especie_animal'
        }),
        label='Espécie Animal',
        required=True
    )
    racas = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'ciclo_especie_animal_racas'
        }),
        label='Raças',
        required=True
    )
    #relacionamentos
    urt = forms.ModelChoiceField(
        queryset=URTs.objects.all(),
        widget=Select2Widget(attrs={
            'class': 'form-select',
        }),
        label='URT',
        required=True,
    )
    observacoes_gerais = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control auto-expand',
            'rows': 1,
            'style': 'padding-top: 25px; height: 120px;',
            'id': 'ciclo_especie_observacoes_gerais'
            }),
        required=False,
        label='Observações Gerais'
    )

    class Meta:
        model = CicloEspeciesVegetaisAnimais
        exclude = ['usuario_registro', 'usuario_atualizacao', 'registro_data', 'ult_atual_data', 'log_n_edicoes', 'del_status', 'del_data', 'del_usuario']

    def save(self, commit=True, *args, **kwargs):
        ciclo_especie = super().save(commit=False, *args, **kwargs)
        if commit:
            ciclo_especie.save()
        return ciclo_especie

class CicloPeriodosClimaticosForm(forms.ModelForm):
    periodo_climatico = forms.ChoiceField(
        choices=PERIODO_CLIMATICO,
        widget=forms.Select(attrs={
            'class': 'form-select',
            'id': 'ciclo_periodo_climatico'
        }),
        label='Tipo de Espécie',
        required=True
    )
    data_inicio = forms.DateField(
        widget=forms.DateInput(attrs={
            'class': 'form-control'
        })
    )
    data_fim = forms.DateField(
        widget=forms.DateInput(attrs={
            'class': 'form-control'
        })
    )
    #relacionamentos
    urt = forms.ModelChoiceField(
        queryset=URTs.objects.all(),
        widget=Select2Widget(attrs={
            'class': 'form-select',
        }),
        label='URT',
        required=True,
    )
    observacoes_gerais = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control auto-expand',
            'rows': 1,
            'style': 'padding-top: 25px; height: 120px;',
            'id': 'ciclo_especie_observacoes_gerais'
            }),
        required=False,
        label='Observações Gerais'
    )

    class Meta:
        model = CicloEspeciesVegetaisAnimais
        exclude = ['usuario_registro', 'usuario_atualizacao', 'registro_data', 'ult_atual_data', 'log_n_edicoes', 'del_status', 'del_data', 'del_usuario']

    def save(self, commit=True, *args, **kwargs):
        ciclo_periodo_climatico = super().save(commit=False, *args, **kwargs)
        if commit:
            ciclo_periodo_climatico.save()
        return ciclo_periodo_climatico

class CicloAtividadesForm(forms.ModelForm):
    fase = forms.ChoiceField(
        choices=CICLO_FASES,
        widget=forms.Select(attrs={
            'class': 'form-select',
            'id': 'ciclo_atividade_fase'
        }),
        label='Fase',
        required=True
    )
    data = forms.DateField(
        widget=forms.DateInput(attrs={
            'class': 'form-control'
        })
    )
    status = forms.ChoiceField(
        choices=CICLO_STATUS_ATIVIDADE,
        widget=forms.Select(attrs={
            'class': 'form-select',
            'id': 'ciclo_atividade_status'
        }),
        label='Fase',
        required=True
    )
    tipo_atividade = forms.ChoiceField(
        choices=CILCO_TIPO_ATIVIDADE,
        widget=forms.Select(attrs={
            'class': 'form-select',
            'id': 'ciclo_atividade_tipo'
        }),
        label='Fase',
        required=True
    )
    descricao_atividade = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control auto-expand',
            'rows': 1,
            'style': 'padding-top: 25px; height: 120px;',
            'id': 'ciclo_atividade_descricao_atividade'
            }),
        required=False,
        label='Descrição da Atividade'
    )
    #relacionamentos
    urt = forms.ModelChoiceField(
        queryset=URTs.objects.all(),
        widget=Select2Widget(attrs={
            'class': 'form-select',
        }),
        label='URT',
        required=True,
    )
    observacoes_gerais = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control auto-expand',
            'rows': 1,
            'style': 'padding-top: 25px; height: 120px;',
            'id': 'ciclo_atividade_observacoes_gerais'
            }),
        required=False,
        label='Observações Gerais'
    )

    class Meta:
        model = CicloAtividades
        exclude = ['usuario_registro', 'usuario_atualizacao', 'registro_data', 'ult_atual_data', 'log_n_edicoes', 'del_status', 'del_data', 'del_usuario']

    def save(self, commit=True, *args, **kwargs):
        ciclo_atividade = super().save(commit=False, *args, **kwargs)
        if commit:
            ciclo_atividade.save()
        return ciclo_atividade


