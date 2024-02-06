from django.db import models
from apps.usuarios.models import Usuarios
from django.utils import timezone
from setup.choices import UNIDADE_DAF2, CNPJ_HIERARQUIA, CNPJ_PORTE, TIPO_DIREITO, FAQ_FORNECEDOR_TOPICO, CARGOS_FUNCOES, GENERO_SEXUAL, TIPO_COMUNICACAO, STATUS_ENVIO_COMUNICACAO

class CNPJ_CNAE(models.Model):
    codigo = models.IntegerField(null=False, blank=False)
    secao_codigo = models.CharField(max_length=10, null=False, blank=False)
    secao_descricao = models.TextField(null=False, blank=False)
    divisao_codigo = models.CharField(max_length=20, null=False, blank=False)
    divisao_descricao = models.TextField( null=False, blank=False)
    grupo_codigo = models.CharField(max_length=20, null=False, blank=False)
    grupo_descricao = models.TextField(null=False, blank=False)
    classe_codigo = models.CharField(max_length=20, null=False, blank=False)
    classe_descricao = models.TextField(null=False, blank=False)
    subclasse_codigo = models.CharField(max_length=20, null=False, blank=False)
    subclasse_descricao = models.TextField(null=False, blank=False)

class CNPJ_NATUREZA_JURIDICA(models.Model):
    codigo = models.CharField(max_length=10, null=False, blank=False)
    tipo = models.CharField(max_length=100, null=False, blank=False)
    natureza_juridica = models.CharField(max_length=100, null=False, blank=False)
    representante_entidade = models.CharField(max_length=100, null=False, blank=False)
    qualificacao = models.CharField(max_length=100, null=False, blank=False)

class UF_Municipio(models.Model):
    cod_ibge = models.CharField(max_length=10, null=False, blank=False)
    uf_sigla = models.CharField(max_length=2, null=False, blank=False)
    uf = models.CharField(max_length=20, null=False, blank=False)
    municipio = models.CharField(max_length=35, null=False, blank=False)
    municipio_uf = models.CharField(max_length=40, null=False, blank=False)
    lat_long = models.CharField(max_length=25, null=False, blank=False)

class Fornecedores(models.Model):
    #relacionamento
    usuario_registro = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING, related_name='fornecedor_registro')
    usuario_atualizacao = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING, related_name='fornecedor_edicao')
    
    #log
    registro_data = models.DateTimeField(auto_now_add=True)
    ult_atual_data = models.DateTimeField(auto_now=True)
    log_n_edicoes = models.IntegerField(default=1)

    #dados do fornecedor
    cnpj = models.CharField(max_length=18, null=False, blank=False)
    hierarquia = models.CharField(max_length=10, choices=CNPJ_HIERARQUIA, null=True, blank=True)
    porte = models.CharField(max_length=20, choices=CNPJ_PORTE, null=False, blank=False)
    tipo_direito = models.CharField(max_length=10, choices=TIPO_DIREITO, null=False, blank=False, default='privado')
    data_abertura = models.DateField(null=True, blank=True)
    natjuridica_codigo = models.CharField(max_length=10, null=True, blank=True)
    natjuridica_descricao = models.CharField(max_length=100, null=True, blank=True)

    #nome do fornecedor
    razao_social = models.CharField(max_length=200, null=False, blank=False, default='Não informado')
    nome_fantasia = models.CharField(max_length=200, null=True, blank=True, default='Não informado')

    #atividade empresarial
    ativ_principal_cod =  models.CharField(max_length=20, null=True, blank=True)
    ativ_principal_descricao =  models.CharField(max_length=200, null=True, blank=True, default='Não informado')

    #endereco
    end_cep = models.CharField(max_length=10, null=True, blank=True)
    end_uf =  models.CharField(max_length=2, null=False, blank=False)
    end_municipio =  models.CharField(max_length=100, null=False, blank=False)
    end_logradouro =  models.CharField(max_length=100, null=True, blank=True, default='Não informado')
    end_numero =  models.CharField(max_length=10, null=True, blank=True, default='NI')
    end_bairro =  models.CharField(max_length=100, null=True, blank=True, default='Não informado')
    
    #observações gerais
    observacoes_gerais = models.TextField(null=True, blank=True, default='Sem observações.')

    #delete (del)
    del_status = models.BooleanField(default=False)
    del_data = models.DateTimeField(null=True, blank=True)
    del_usuario = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='fornecedor_deletado')

    def save(self, *args, **kwargs):
        user = kwargs.pop('current_user', None)  # Obtenha o usuário atual e remova-o dos kwargs

        # Se o objeto já tem um ID, então ele já existe no banco de dados
        if self.id:
            self.log_n_edicoes += 1
            if user:
                self.usuario_atualizacao = user
        else:
            if user:
                self.usuario_registro = user
                self.usuario_atualizacao = user
        super(Fornecedores, self).save(*args, **kwargs)


    def soft_delete(self, user):
        """
        Realiza uma "deleção lógica" do registro.
        """
        self.del_status = True
        self.del_data = timezone.now()
        self.del_usuario = user
        self.save()
    
    def __str__(self):
        return f"{self.nome_fantasia} ({self.cnpj})"

class Fornecedores_Faq(models.Model):
    #relacionamento
    usuario_registro = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING, related_name='fornecedor_faq_registro')
    usuario_atualizacao = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING, related_name='fornecedor_faq_edicao')
    
    #log
    registro_data = models.DateTimeField(auto_now_add=True)
    ult_atual_data = models.DateTimeField(auto_now=True)
    log_n_edicoes = models.IntegerField(default=1)

    #dados do FAQ
    topico = models.CharField(max_length=30, choices=FAQ_FORNECEDOR_TOPICO, null=False, blank=False)
    topico_outro = models.CharField(max_length=100, null=True, blank=True)
    contexto = models.TextField(null=True, blank=True)
    resposta = models.TextField(null=True, blank=True)
    
    #observações gerais
    observacoes_gerais = models.TextField(null=True, blank=True, default='Sem observações.')

    #delete (del)
    del_status = models.BooleanField(default=False)
    del_data = models.DateTimeField(null=True, blank=True)
    del_usuario = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='fornecedor_faq_deletado')

    def save(self, *args, **kwargs):
        user = kwargs.pop('current_user', None)  # Obtenha o usuário atual e remova-o dos kwargs

        # Se o objeto já tem um ID, então ele já existe no banco de dados
        if self.id:
            self.log_n_edicoes += 1
            if user:
                self.usuario_atualizacao = user
        else:
            if user:
                self.usuario_registro = user
                self.usuario_atualizacao = user
        super(Fornecedores_Faq, self).save(*args, **kwargs)


    def soft_delete(self, user):
        """
        Realiza uma "deleção lógica" do registro.
        """
        self.del_status = True
        self.del_data = timezone.now()
        self.del_usuario = user
        self.save()

class Fornecedores_Representantes(models.Model):
    #relacionamento
    usuario_registro = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING, related_name='fornecedor_representante_registro')
    usuario_atualizacao = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING, related_name='fornecedor_representante_edicao')
    fornecedor = models.ForeignKey(Fornecedores, on_delete=models.DO_NOTHING, related_name='fornecedor_representante')

    #log
    registro_data = models.DateTimeField(auto_now_add=True)
    ult_atual_data = models.DateTimeField(auto_now=True)
    log_n_edicoes = models.IntegerField(default=1)

    #dados do Representante
    cpf = models.CharField(max_length=14, null=True, blank=True)
    nome_completo = models.CharField(max_length=100, null=False, blank=False)
    data_nascimento = models.DateField(null=True, blank=True)
    genero_sexual = models.CharField(max_length=20, choices=GENERO_SEXUAL, null=True, blank=True)
    cargo = models.CharField(max_length=30, choices=CARGOS_FUNCOES, null=True, blank=True)
    cargo_outro = models.CharField(max_length=100, null=True, blank=True)
    telefone = models.CharField(max_length=14, null=True, blank=True)
    celular = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    
    #observações gerais
    observacoes_gerais = models.TextField(null=True, blank=True, default='Sem observações.')

    #delete (del)
    del_status = models.BooleanField(default=False)
    del_data = models.DateTimeField(null=True, blank=True)
    del_usuario = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='fornecedor_representante_deletado')

    def save(self, *args, **kwargs):
        user = kwargs.pop('current_user', None)  # Obtenha o usuário atual e remova-o dos kwargs

        # Se o objeto já tem um ID, então ele já existe no banco de dados
        if self.id:
            self.log_n_edicoes += 1
            if user:
                self.usuario_atualizacao = user
        else:
            if user:
                self.usuario_registro = user
                self.usuario_atualizacao = user
        super(Fornecedores_Representantes, self).save(*args, **kwargs)


    def soft_delete(self, user):
        """
        Realiza uma "deleção lógica" do registro.
        """
        self.del_status = True
        self.del_data = timezone.now()
        self.del_usuario = user
        self.save()

class Fornecedores_Comunicacoes(models.Model):
    #relacionamento
    usuario_registro = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING, related_name='fornecedor_comunicacao_registro')
    usuario_atualizacao = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING, related_name='fornecedor_comunicacao_edicao')
    fornecedor = models.ForeignKey(Fornecedores, on_delete=models.DO_NOTHING, related_name='fornecedor_comunicacao')

    #log
    registro_data = models.DateTimeField(auto_now_add=True)
    ult_atual_data = models.DateTimeField(auto_now=True)
    log_n_edicoes = models.IntegerField(default=1)

    #dados do Representante
    unidade_daf = models.CharField(max_length=15, choices=UNIDADE_DAF2, null=False, blank=False)
    tipo_comunicacao = models.CharField(max_length=25, choices=TIPO_COMUNICACAO, null=False, blank=False)
    topico_comunicacao = models.CharField(max_length=40, choices=FAQ_FORNECEDOR_TOPICO, null=True, blank=True)
    assunto = models.CharField(max_length=200, null=True, blank=True)
    demanda_original = models.TextField(null=True, blank=True)
    destinatario = models.TextField(null=True, blank=True)
    mensagem_encaminhada = models.TextField(null=True, blank=True)
    status_envio = models.CharField(max_length=40, choices=STATUS_ENVIO_COMUNICACAO, null=True, blank=True)
    data_envio = models.DateField(null=True, blank=True)
    responsavel_resposta = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING, related_name='fornecedor_comunicacao_responsavel', null=True, blank=True)
    outro_responsavel = models.CharField(max_length=80, null=True, blank=True)
    
    #observações gerais
    observacoes_gerais = models.TextField(null=True, blank=True, default='Sem observações.')

    #delete (del)
    del_status = models.BooleanField(default=False)
    del_data = models.DateTimeField(null=True, blank=True)
    del_usuario = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='fornecedor_comunicacao_deletado')

    def save(self, *args, **kwargs):
        user = kwargs.pop('current_user', None)  # Obtenha o usuário atual e remova-o dos kwargs

        # Se o objeto já tem um ID, então ele já existe no banco de dados
        if self.id:
            self.log_n_edicoes += 1
            if user:
                self.usuario_atualizacao = user
        else:
            if user:
                self.usuario_registro = user
                self.usuario_atualizacao = user
        super(Fornecedores_Comunicacoes, self).save(*args, **kwargs)


    def soft_delete(self, user):
        """
        Realiza uma "deleção lógica" do registro.
        """
        self.del_status = True
        self.del_data = timezone.now()
        self.del_usuario = user
        self.save()