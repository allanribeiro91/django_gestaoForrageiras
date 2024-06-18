from django.db import models
from apps.usuarios.models import Usuarios
from datetime import timedelta
from django.utils import timezone
from setup.choices import (LISTA_UFS_SIGLAS, LISTA_TEXTURA_SOLO, LISTA_MESES, 
                           ESPECIES_ANIMAIS, ESPECIES_VEGETAIS, LOCAL_PREPARO_AMOSTRAS,
                           STATUS_CONTRATOS_TECNICOS, FORMACAO_TECNICA, PERIODO_CLIMATICO,
                           CICLO_FASES, CICLO_TIPO_ATIVIDADE, CICLO_STATUS_ATIVIDADE,
                           TIPO_ESPECIE, CICLO_STATUS, FASE_PROJETO_FORRAGEIRAS
                        )

#URT
class URTs(models.Model):
    #relacionamento
    usuario_registro = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING, related_name='usuario_urt_registro')
    usuario_atualizacao = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING, related_name='usuario_urt_edicao')
    
    #log
    registro_data = models.DateTimeField(auto_now_add=True)
    ult_atual_data = models.DateTimeField(auto_now=True)
    log_n_edicoes = models.IntegerField(default=1)

    #propriedade
    nome_propriedade = models.CharField(max_length=120, null=True, blank=True)
    proprietario_nome = models.CharField(max_length=120, null=True, blank=True)
    proprietario_telefone = models.CharField(max_length=15, null=True, blank=True)
    proprietario_celular = models.CharField(max_length=15, null=True, blank=True)
    proprietario_email = models.EmailField(max_length=80, null=True, blank=True)
    
    #localizacao
    uf = models.CharField(max_length=2, choices=LISTA_UFS_SIGLAS, null=False, blank=False)
    municipio = models.CharField(max_length=120, null=False, blank=False)
    endereco = models.TextField(null=True, blank=True)
    latlong = models.CharField(max_length=60, null=True, blank=True)
    pluscode = models.CharField(max_length=60, null=True, blank=True)

    #caracteristicas gerais
    area_experimento = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    textura_solo = models.CharField(max_length=30, choices=LISTA_TEXTURA_SOLO, null=True, blank=True)
    local_preparo_amostras = models.CharField(max_length=120, choices=LOCAL_PREPARO_AMOSTRAS, null=True, blank=True)

    #clima
    precipitacao_anual = models.IntegerField(null=True, blank=True)
    periodo_chuva_inicio = models.IntegerField(choices=LISTA_MESES, null=True, blank=True)
    periodo_chuva_fim = models.IntegerField(choices=LISTA_MESES, null=True, blank=True)
    periodo_seca_inicio = models.IntegerField(choices=LISTA_MESES, null=True, blank=True)
    periodo_seca_fim = models.IntegerField(choices=LISTA_MESES, null=True, blank=True)
    
    #dados da federacao
    federacao_presidente = models.CharField(max_length=120, null=True, blank=True)
    federacao_telefone = models.CharField(max_length=15, null=True, blank=True)
    federacao_email = models.EmailField(max_length=80, null=True, blank=True)

    #dados senar
    senar_superintendente = models.CharField(max_length=120, null=True, blank=True)
    senar_telefone = models.CharField(max_length=15, null=True, blank=True)
    senar_email = models.EmailField(max_length=80, null=True, blank=True)

    #supervisor URT
    supervisor_nome = models.CharField(max_length=120, null=True, blank=True)
    supervisor_telefone = models.CharField(max_length=15, null=True, blank=True)
    supervisor_email = models.EmailField(max_length=80, null=True, blank=True)

    #observacoes
    observacoes_gerais = models.TextField(null=True, blank=True, default='Sem observações.')

    #delete (del)
    del_status = models.BooleanField(default=False)
    del_data = models.DateTimeField(null=True, blank=True)
    del_usuario = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='usuario_urt_deletado')

    def save(self, *args, **kwargs):
        user = kwargs.pop('current_user', None)
        if self.id:
            self.log_n_edicoes += 1
            if user:
                self.usuario_atualizacao = user
        else:
            if user:
                self.usuario_registro = user
                self.usuario_atualizacao = user
        super(URTs, self).save(*args, **kwargs)


    def soft_delete(self, user):
        self.del_status = True
        self.del_data = timezone.now()
        self.del_usuario = user
        self.save()

    def tecnico_atual(self):
        # Filtra os técnicos associados a esta URT com status 'em_execucao'
        tecnicos = TecnicoURT.objects.filter(urt=self, status_contrato='em_execucao', del_status=False)

        # Retorna os dados do primeiro técnico encontrado ou None se nenhum for encontrado
        if tecnicos.exists():
            tecnico = tecnicos.first()
            dados_tecnico = {
                'tecnico': tecnico.tecnico,
                'formacao': tecnico.get_formacao_tecnica_display,
                'celular': tecnico.celular,
                'email': tecnico.email,
                'status_contrato': tecnico.status_contrato,
                'data_inicio': tecnico.data_inicio,
                'data_fim': tecnico.data_fim
            }
            return dados_tecnico
        else:
            return None

    def especies_vegetais_urt(self):
        especies_vegetais = URTespecieVegetal.objects.filter(urt=self, del_status=False)
        lista_especies = [especie.especies_variedades() for especie in especies_vegetais]
        return ';<br> '.join(lista_especies)
    
    def especies_animais_urt(self):
        especies_animais = URTespecieAnimal.objects.filter(urt=self, del_status=False)
        lista_especies = [especie.especies_racas() for especie in especies_animais]
        return ';<br> '.join(lista_especies)

    def __str__(self):
        return f"URT: {self.municipio}-{self.uf}"


#ESPÉCIES VEGETAIS E ANIMAIS
class URTespecieVegetal(models.Model):
    #relacionamento
    usuario_registro = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING, related_name='usuario_urt_vegetal_registro')
    usuario_atualizacao = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING, related_name='usuario_urt_vegetal_edicao')
    
    #log
    registro_data = models.DateTimeField(auto_now_add=True)
    ult_atual_data = models.DateTimeField(auto_now=True)
    log_n_edicoes = models.IntegerField(default=1)

    #dados da especie vegetal
    especie_vegetal = models.CharField(max_length=120, choices=ESPECIES_VEGETAIS, null=True, blank=True)
    variedades = models.TextField(null=True, blank=True)
    area_utilizada = models.FloatField(null=True, blank=True, default=0)
    producao_silagem = models.BooleanField(null=True, blank=True)
    
    #relacionamento
    urt = models.ForeignKey(URTs, on_delete=models.DO_NOTHING, related_name='urt_especie_vegetal')

    #observacoes
    observacoes_gerais = models.TextField(null=True, blank=True, default='Sem observações.')

    #delete (del)
    del_status = models.BooleanField(default=False)
    del_data = models.DateTimeField(null=True, blank=True)
    del_usuario = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='usuario_urt_vegetal_deletado')

    def save(self, *args, **kwargs):
        user = kwargs.pop('current_user', None)

        # Se o objeto já tem um ID, então ele já existe no banco de dados
        if self.id:
            self.log_n_edicoes += 1
            if user:
                self.usuario_atualizacao = user
        else:
            if user:
                self.usuario_registro = user
                self.usuario_atualizacao = user
        super(URTespecieVegetal, self).save(*args, **kwargs)

    def soft_delete(self, user):
        self.del_status = True
        self.del_data = timezone.now()
        self.del_usuario = user
        self.save()

    def especies_variedades(self):
        especie_display = self.get_especie_vegetal_display()
        return f"{especie_display}: {self.variedades}"

    def __str__(self):
        return f"URT: {self.urt.municipio}-{self.urt.uf} - Espécies Vegetais: {self.especie_vegetal}"

class URTespecieAnimal(models.Model):
    #relacionamento
    usuario_registro = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING, related_name='usuario_urt_animal_registro')
    usuario_atualizacao = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING, related_name='usuario_urt_animal_edicao')
    
    #log
    registro_data = models.DateTimeField(auto_now_add=True)
    ult_atual_data = models.DateTimeField(auto_now=True)
    log_n_edicoes = models.IntegerField(default=1)

    #dados da especie animal
    especie_animal = models.CharField(max_length=120, choices=ESPECIES_ANIMAIS, null=True, blank=True)
    racas = models.TextField(null=True, blank=True)
    area_utilizada = models.FloatField(null=True, blank=True, default=0)
    
    #relacionamento
    urt = models.ForeignKey(URTs, on_delete=models.DO_NOTHING, related_name='urt_especie_animal')

    #observacoes
    observacoes_gerais = models.TextField(null=True, blank=True, default='Sem observações.')

    #delete (del)
    del_status = models.BooleanField(default=False)
    del_data = models.DateTimeField(null=True, blank=True)
    del_usuario = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='usuario_urt_animal_deletado')

    def save(self, *args, **kwargs):
        user = kwargs.pop('current_user', None)

        # Se o objeto já tem um ID, então ele já existe no banco de dados
        if self.id:
            self.log_n_edicoes += 1
            if user:
                self.usuario_atualizacao = user
        else:
            if user:
                self.usuario_registro = user
                self.usuario_atualizacao = user
        super(URTespecieAnimal, self).save(*args, **kwargs)

    def soft_delete(self, user):
        self.del_status = True
        self.del_data = timezone.now()
        self.del_usuario = user
        self.save()
    
    def especies_racas(self):
        especie_display = self.get_especie_animal_display()
        return f"{especie_display}: {self.racas}"

    def __str__(self):
        return f"URT: {self.urt.municipio}-{self.urt.uf} - Espécies Animais: {self.especie_animal}"


#TÉCNICOS DA URT
class TecnicoURT (models.Model):
    #relacionamento
    usuario_registro = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING, related_name='usuario_urt_tecnico_registro')
    usuario_atualizacao = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING, related_name='usuario_urt_tecnico_edicao')
    
    #log
    registro_data = models.DateTimeField(auto_now_add=True)
    ult_atual_data = models.DateTimeField(auto_now=True)
    log_n_edicoes = models.IntegerField(default=1)

    #dados do contrato
    status_contrato = models.CharField(max_length=20, choices=STATUS_CONTRATOS_TECNICOS, blank=False, null=False, default='nao_informado')
    numero_contrato = models.CharField(max_length=10, blank=True, null=True)
    data_inicio = models.DateField(blank=True, null=True)
    data_fim = models.DateField(blank=True, null=True)

    #dados da empresa
    cnpj = models.CharField(max_length=18, null=True, blank=True)
    razao_social = models.CharField(max_length=200, null=False, blank=False, default='Não informado')
    nome_fantasia = models.CharField(max_length=200, null=False, blank=False, default='Não informado')
    
    #dados do técnico
    cpf = models.CharField(max_length=14, null=True, blank=True)
    tecnico = models.CharField(max_length=100, null=False, blank=False, default='Não Informado')
    formacao_tecnica = models.CharField(max_length=20, choices=FORMACAO_TECNICA, blank=False, null=False, default='nao_informado')
    celular = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(max_length=80, null=True, blank=True)

    #observacoes
    observacoes_gerais = models.TextField(null=True, blank=True, default='Sem observações.')

    #relacionamento
    urt = models.ForeignKey(URTs, on_delete=models.DO_NOTHING, related_name='urt_tecnico')

    #delete (del)
    del_status = models.BooleanField(default=False)
    del_data = models.DateTimeField(null=True, blank=True)
    del_usuario = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='usuario_urt_tecnico_deletado')

    def save(self, *args, **kwargs):
        user = kwargs.pop('current_user', None)

        # Se o objeto já tem um ID, então ele já existe no banco de dados
        if self.id:
            self.log_n_edicoes += 1
            if user:
                self.usuario_atualizacao = user
        else:
            if user:
                self.usuario_registro = user
                self.usuario_atualizacao = user
        super(TecnicoURT, self).save(*args, **kwargs)

    def soft_delete(self, user):
        self.del_status = True
        self.del_data = timezone.now()
        self.del_usuario = user
        self.save()

    def __str__(self):
        return f"URT: {self.urt.municipio}-{self.urt.uf} - Técnico: {self.tecnico}"


#CICLOS
class Ciclo (models.Model):
    #relacionamento
    usuario_registro = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING, related_name='usuario_ciclo_registro')
    usuario_atualizacao = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING, related_name='usuario_ciclo_edicao')
    
    #log
    registro_ddata_ata = models.DateTimeField(auto_now_add=True)
    ult_atual_data = models.DateTimeField(auto_now=True)
    log_n_edicoes = models.IntegerField(default=1)

    #dados do ciclo
    fase_projeto = models.CharField(max_length=60, choices=FASE_PROJETO_FORRAGEIRAS, null=False, blank=False)
    numero_ciclo = models.IntegerField(null=False, blank=False)
    status_ciclo = models.CharField(max_length=60, choices=CICLO_STATUS, null=False, blank=False)
    fase1_inicio = models.DateField(null=True, blank=True)
    fase1_fim = models.DateField(null=True, blank=True)
    fase2_inicio = models.DateField(null=True, blank=True)
    fase2_fim = models.DateField(null=True, blank=True)
    fase3_inicio = models.DateField(null=True, blank=True)
    fase3_fim = models.DateField(null=True, blank=True)
    
    #observacoes
    observacoes_gerais = models.TextField(null=True, blank=True, default='Sem observações.')

    #relacionamento
    urt = models.ForeignKey(URTs, on_delete=models.DO_NOTHING, related_name='urt_ciclo')

    #delete (del)
    del_status = models.BooleanField(default=False)
    del_data = models.DateTimeField(null=True, blank=True)
    del_usuario = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='usuario_ciclo_deletado')

    def save(self, *args, **kwargs):
        user = kwargs.pop('current_user', None)

        # Se o objeto já tem um ID, então ele já existe no banco de dados
        if self.id:
            self.log_n_edicoes += 1
            if user:
                self.usuario_atualizacao = user
        else:
            if user:
                self.usuario_registro = user
                self.usuario_atualizacao = user
        super(Ciclo, self).save(*args, **kwargs)

    def soft_delete(self, user):
        self.del_status = True
        self.del_data = timezone.now()
        self.del_usuario = user
        self.save()

    def __str__(self):
        return f"Ciclo: {self.numero_ciclo}, URT: {self.urt.municipio}-{self.urt.uf}"

class CicloEspecieVegetal (models.Model):
    #relacionamento
    usuario_registro = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING, related_name='usuario_ciclo_especie_vegetal_registro')
    usuario_atualizacao = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING, related_name='usuario_ciclo_especie_vegetal_edicao')
    
    #log
    registro_data = models.DateTimeField(auto_now_add=True)
    ult_atual_data = models.DateTimeField(auto_now=True)
    log_n_edicoes = models.IntegerField(default=1)

    #dados da espécie VEGETAL
    especie_vegetal = models.CharField(max_length=140, choices=ESPECIES_VEGETAIS, null=True, blank=True)
    variedades = models.CharField(max_length=140, null=True, blank=True)
    area_utilizada = models.FloatField(null=True, blank=True, default=0)
    producao_silagem = models.BooleanField(null=True, blank=True)
    
    #observacoes
    observacoes_gerais = models.TextField(null=True, blank=True, default='Sem observações.')

    #relacionamento
    urt = models.ForeignKey(URTs, on_delete=models.DO_NOTHING, related_name='urt_ciclo_especie_vegetal')
    ciclo = models.ForeignKey(Ciclo, on_delete=models.DO_NOTHING, related_name='ciclo_especie_vegetal')

    #delete (del)
    del_status = models.BooleanField(default=False)
    del_data = models.DateTimeField(null=True, blank=True)
    del_usuario = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='usuario_ciclo_especie_vegetal_deletado')

    def save(self, *args, **kwargs):
        user = kwargs.pop('current_user', None)

        # Se o objeto já tem um ID, então ele já existe no banco de dados
        if self.id:
            self.log_n_edicoes += 1
            if user:
                self.usuario_atualizacao = user
        else:
            if user:
                self.usuario_registro = user
                self.usuario_atualizacao = user
        super(CicloEspecieVegetal, self).save(*args, **kwargs)

    def soft_delete(self, user):
        self.del_status = True
        self.del_data = timezone.now()
        self.del_usuario = user
        self.save()

    def __str__(self):
        return f"Espécies Vegetais: {self.especie_vegetal}, Variedades: {self.variedades}, Ciclo: {self.ciclo.numero_ciclo}, URT: {self.urt.municipio}-{self.urt.uf}"

class CicloEspecieAnimal (models.Model):
    #relacionamento
    usuario_registro = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING, related_name='usuario_ciclo_especie_animal_registro')
    usuario_atualizacao = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING, related_name='usuario_ciclo_especie_animal_edicao')
    
    #log
    registro_data = models.DateTimeField(auto_now_add=True)
    ult_atual_data = models.DateTimeField(auto_now=True)
    log_n_edicoes = models.IntegerField(default=1)

    #dados da espécie ANIMAL
    especie_animal = models.CharField(max_length=140, choices=ESPECIES_ANIMAIS, null=False, blank=False)
    racas = models.CharField(max_length=140, null=True, blank=True)
    area_utilizada = models.FloatField(null=True, blank=True, default=0)
    
    #observacoes
    observacoes_gerais = models.TextField(null=True, blank=True, default='Sem observações.')

    #relacionamento
    urt = models.ForeignKey(URTs, on_delete=models.DO_NOTHING, related_name='urt_ciclo_especie_animal')
    ciclo = models.ForeignKey(Ciclo, on_delete=models.DO_NOTHING, related_name='ciclo_especie_animal')

    #delete (del)
    del_status = models.BooleanField(default=False)
    del_data = models.DateTimeField(null=True, blank=True)
    del_usuario = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='usuario_ciclo_especie_animal_deletado')

    def save(self, *args, **kwargs):
        user = kwargs.pop('current_user', None)

        # Se o objeto já tem um ID, então ele já existe no banco de dados
        if self.id:
            self.log_n_edicoes += 1
            if user:
                self.usuario_atualizacao = user
        else:
            if user:
                self.usuario_registro = user
                self.usuario_atualizacao = user
        super(CicloEspecieAnimal, self).save(*args, **kwargs)

    def soft_delete(self, user):
        self.del_status = True
        self.del_data = timezone.now()
        self.del_usuario = user
        self.save()

    def __str__(self):
        return f"Espécies Animais: {self.especie_animal}, Raças: {self.racas}, Ciclo: {self.ciclo.numero_ciclo}, URT: {self.urt.municipio}-{self.urt.uf}"

class CicloAtividades (models.Model):
    #relacionamento
    usuario_registro = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING, related_name='usuario_ciclo_atividade_registro')
    usuario_atualizacao = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING, related_name='usuario_ciclo_atividade_edicao')
    
    #log
    registro_data = models.DateTimeField(auto_now_add=True)
    ult_atual_data = models.DateTimeField(auto_now=True)
    log_n_edicoes = models.IntegerField(default=1)

    #dados da Atividade
    ciclo_fase = models.CharField(max_length=30, choices=CICLO_FASES, null=False, blank=False)
    data = models.DateField(null=False, blank=False)
    status = models.CharField(max_length=20, choices=CICLO_STATUS_ATIVIDADE, null=False, blank=False)
    tipo_atividade = models.CharField(max_length=40, choices=CICLO_TIPO_ATIVIDADE, null=False, blank=False)
    descricao_atividade = models.TextField(null=True, blank=True, default='Não informado.')
    anexo_titulo = models.CharField(max_length=100, blank=True, null=True)
    anexo_url = models.URLField(null=True, blank=True)

    #observacoes
    observacoes_gerais = models.TextField(null=True, blank=True, default='Sem observações.')

    #relacionamento
    urt = models.ForeignKey(URTs, on_delete=models.DO_NOTHING, related_name='urt_ciclo_atividade')
    ciclo = models.ForeignKey(Ciclo, on_delete=models.DO_NOTHING, related_name='ciclo_atividade')

    #delete (del)
    del_status = models.BooleanField(default=False)
    del_data = models.DateTimeField(null=True, blank=True)
    del_usuario = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='usuario_ciclo_atividade_deletado')

    def save(self, *args, **kwargs):
        user = kwargs.pop('current_user', None)

        # Se o objeto já tem um ID, então ele já existe no banco de dados
        if self.id:
            self.log_n_edicoes += 1
            if user:
                self.usuario_atualizacao = user
        else:
            if user:
                self.usuario_registro = user
                self.usuario_atualizacao = user
        super(CicloAtividades, self).save(*args, **kwargs)

    def soft_delete(self, user):
        self.del_status = True
        self.del_data = timezone.now()
        self.del_usuario = user
        self.save()

    def __str__(self):
        return f"Atividade: {self.tipo_atividade}, Data: {self.data}, Ciclo: {self.ciclo.numero_ciclo}, URT: {self.urt.municipio}-{self.urt.uf}"

