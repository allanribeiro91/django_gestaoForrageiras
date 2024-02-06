from django.db import models
from apps.usuarios.models import Usuarios
from setup.choices import TIPO_PRODUTO, FORMA_FARMACEUTICA, STATUS_INCORPORACAO, CONCENTRACAO_TIPO, CLASSIFICACAO_AWARE
from django.utils import timezone

class DenominacoesGenericas(models.Model):
     # relacionamento
    usuario_registro = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING, related_name='denominacoes_registradas')
    usuario_atualizacao = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING, related_name='denominacoes_editadas')
    
    # log
    registro_data = models.DateTimeField(auto_now_add=True)
    ult_atual_data = models.DateTimeField(auto_now=True)
    log_n_edicoes = models.IntegerField(default=1)

    #denominação genérica
    denominacao = models.CharField(max_length=140, null=False, blank=False)
    tipo_produto = models.CharField(max_length=15, choices=TIPO_PRODUTO, null=True, blank=True)

    #unidades do DAF que a denominação genérica é utilizada
    unidade_basico = models.BooleanField(default=False, null=False, blank=False, db_index=True)
    unidade_especializado = models.BooleanField(default=False, null=False, blank=False, db_index=True)
    unidade_estrategico = models.BooleanField(default=False, null=False, blank=False, db_index=True)
    unidade_farm_popular = models.BooleanField(default=False, null=False, blank=False, db_index=True)
    hospitalar = models.BooleanField(default=False, null=False, blank=False, db_index=True)
    
    #observações gerais
    observacoes_gerais = models.TextField(null=True, blank=True)

    #delete (del)
    del_status = models.BooleanField(default=False)
    del_data = models.DateTimeField(null=True, blank=True)
    del_usuario = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='denominacoes_deletadas')

    def get_denominacao_nome(self):
        return self.denominacao

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
        super(DenominacoesGenericas, self).save(*args, **kwargs)


    def soft_delete(self, user):
        self.del_status = True
        self.del_data = timezone.now()
        self.del_usuario = user
        self.save()
    
    @property
    def componentes_af(self):        
        unidades = []
        if self.unidade_basico:
            unidades.append("cgafb")
        if self.unidade_especializado:
            unidades.append("cgceaf")
        if self.unidade_estrategico:
            unidades.append("cgafme")
        if self.unidade_farm_popular:
            unidades.append("cgfp")
        if self.hospitalar:
            unidades.append("hospitalar")
        return unidades


    def __str__(self):
        return f"{self.denominacao} (ID: {self.id})"

class ProdutosFarmaceuticos(models.Model):
    #relacionamento
    usuario_registro = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING, related_name='usuario_registro_produto')
    usuario_atualizacao = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING, related_name='usuario_atualizacao_produto')
    denominacao = models.ForeignKey(DenominacoesGenericas, on_delete=models.DO_NOTHING, related_name='denominacao_produto')

    #log
    registro_data = models.DateTimeField(auto_now_add=True)
    ult_atual_data = models.DateTimeField(auto_now=True)
    log_n_edicoes = models.IntegerField(default=1)

    #dados do produto farmacêutico
    produto = models.TextField(null=False, blank=False)
    concentracao_tipo = models.CharField(max_length=20, choices=CONCENTRACAO_TIPO, null=False, blank=False)
    concentracao = models.TextField(null=False, blank=False)
    forma_farmaceutica = models.CharField(max_length=60, choices=FORMA_FARMACEUTICA, null=False, blank=False)
    oncologico = models.BooleanField(default=False, null=True, blank=True)
    biologico = models.BooleanField(default=False, null=True, blank=True)
    aware = models.CharField(max_length=20, choices=CLASSIFICACAO_AWARE, null=True, blank=True)
    atc = models.CharField(max_length=20, null=True, blank=True)
    atc_descricao = models.CharField(max_length=100, null=True, blank=True)
    
    #incorporacao SUS
    incorp_status = models.CharField(max_length=20, choices=STATUS_INCORPORACAO, null=True, blank=True)
    incorp_data = models.DateField(null=True, blank=True)
    incorp_portaria = models.CharField(max_length=30, null=True, blank=True)
    incorp_link = models.URLField(max_length=100, null=True, blank=True)
    exclusao_data = models.DateField(null=True, blank=True)
    exclusao_portaria = models.CharField(max_length=30, null=True, blank=True)
    exclusao_link = models.URLField(max_length=100, null=True, blank=True)

    #pactuacao
    comp_basico = models.BooleanField(default=False, null=True, blank=True)
    comp_especializado = models.BooleanField(default=False, null=True, blank=True)
    comp_estrategico = models.BooleanField(default=False, null=True, blank=True)

    #outros
    disp_farmacia_popular = models.BooleanField(default=False, null=True, blank=True)
    hospitalar = models.BooleanField(default=False, null=True, blank=True)
    
    #outros sistemas
    sigtap_possui = models.BooleanField(default=False, null=True, blank=True)
    sigtap_codigo = models.CharField(max_length=10, null=True, blank=True)
    sigtap_nome = models.CharField(max_length=60, null=True, blank=True)
    sismat_possui = models.BooleanField(default=False, null=True, blank=True)
    sismat_codigo = models.CharField(max_length=10, null=True, blank=True)
    sismat_nome = models.CharField(max_length=60, null=True, blank=True)
    catmat_possui = models.BooleanField(default=False, null=True, blank=True)
    catmat_codigo = models.CharField(max_length=10, null=True, blank=True)
    catmat_nome = models.CharField(max_length=60, null=True, blank=True)
    obm_possui = models.BooleanField(default=False, null=True, blank=True)
    obm_codigo = models.CharField(max_length=10, null=True, blank=True)
    obm_nome = models.CharField(max_length=60, null=True, blank=True)
    
    #observações gerais
    observacoes_gerais = models.TextField(null=True, blank=True)

    #delete (del)
    del_status = models.BooleanField(default=False)
    del_data = models.DateTimeField(null=True, blank=True)
    del_usuario = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='usuario_produto_deletado')

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
        super(ProdutosFarmaceuticos, self).save(*args, **kwargs)

    def soft_delete(self, user):
        """
        Realiza uma "deleção lógica" do registro.
        """
        self.del_status = True
        self.del_data = timezone.now()
        self.del_usuario = user
        self.save()

    @classmethod
    def get_produtos_por_denominacao(cls, denominacao):
        produtos = cls.objects.filter(denominacao_id=denominacao, del_status=False).values('id', 'produto')
        return list(produtos)

    def __str__(self):
        return f"{self.produto} - ID: {self.id}"

class Tags(models.Model):
    tag = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"Tag: {self.tag} - ID ({self.id})"

class ListaATC(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    nivel = models.CharField(max_length=2)
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return f"ATC: {self.codigo} - {self.nivel} - {self.descricao} - ID ({self.id}) )"

class ProdutosTagsManager(models.Manager):
    def active(self):
        return self.filter(del_status=False)

class ProdutosTags(models.Model):
    #relacionamento usuario
    usuario_registro = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING, related_name='usuario_registro_tag')
    usuario_atualizacao = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING, related_name='usuario_atualizacao_tag')

    #relacionamento produto
    produto = models.ForeignKey(ProdutosFarmaceuticos, on_delete=models.DO_NOTHING, related_name='produto_tag')

    #tag
    tag_id = models.IntegerField(default=None)
    tag = models.CharField(max_length=255)

    #log
    registro_data = models.DateTimeField(auto_now_add=True)
    ult_atual_data = models.DateTimeField(auto_now=True)
    log_n_edicoes = models.IntegerField(default=1)

    #delete (del)
    del_status = models.BooleanField(default=False)
    del_data = models.DateTimeField(null=True, blank=True)
    del_usuario = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='usuario_produtotag_deletado')

    def soft_delete(self, usuario_instance):
        if self.del_status:
            return  # Se já estiver deletado, simplesmente retorne e não faça nada
        self.del_status = True
        self.del_data = timezone.now()
        self.del_usuario = usuario_instance
        self.save()
    
    def reverse_soft_delete(self):
        self.del_status = False
        self.del_data = None
        self.del_usuario = None
        self.save()

    def __str__(self):
        return f"Produto/Tag: {self.produto} - Tag ({self.tag})"
    
    objects = ProdutosTagsManager()

class ProdutoConsumoMedio(models.Model):
    #relacionamento usuario
    usuario_registro = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING, related_name='usuario_registro_cmm')

    #log
    registro_data = models.DateTimeField(auto_now_add=True)

    #relacionamento produto
    produto = models.ForeignKey(ProdutosFarmaceuticos, on_delete=models.DO_NOTHING, related_name='produto_cmm')

    #dados
    tipo_cmm = models.CharField(max_length=20, null=False, blank=False)
    data_referencia = models.DateField(null=False, blank=False)
    periodo_referencia = models.CharField(max_length=10, null=True, blank=True)
    estoque_ses = models.FloatField(null=False, blank=False)
    aprovado_administrativo = models.FloatField(null=False, blank=False)
    aprovado_judicial = models.FloatField(null=False, blank=False)
    aprovado_total = models.FloatField(null=False, blank=False, default=0)
    cmm_administrativo = models.FloatField(null=False, blank=False)
    cmm_judicial = models.FloatField(null=False, blank=False)
    cmm_total = models.FloatField(null=False, blank=False)
    observacoes = models.TextField(null=True, blank=True, default='Sem observações.')
    responsavel_dados = models.CharField(max_length=20, null=False, blank=False)