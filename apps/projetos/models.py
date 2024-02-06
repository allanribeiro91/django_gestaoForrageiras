from django.db import models
from apps.usuarios.models import Usuarios
from datetime import timedelta
from django.utils import timezone
from setup.choices import LISTA_UFS_SIGLAS, STATUS_PROJETO, SUBPROGRAMA, ATIVIDADES_ATEG

class Projetos(models.Model):
    #relacionamento
    usuario_registro = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING, related_name='usuario_projeto_registro')
    usuario_atualizacao = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING, related_name='usuario_projeto_edicao')
    
    #log
    registro_data = models.DateTimeField(auto_now_add=True)
    ult_atual_data = models.DateTimeField(auto_now=True)
    log_n_edicoes = models.IntegerField(default=1)

    #dados administrativos
    id_projeto_sisateg = models.CharField(max_length=40, null=True, blank=True)
    regional = models.CharField(max_length=2, choices=LISTA_UFS_SIGLAS, null=False, blank=False)
    status = models.CharField(max_length=20, choices=STATUS_PROJETO, null=False, blank=False)
    nome_plano_trabalho = models.TextField(null=False, blank=False)
    n_processo = models.CharField(max_length=40, null=True, blank=True)
    termo_adesao = models.CharField(max_length=40, null=True, blank=True)
    n_plano_trabalho = models.CharField(max_length=40, null=True, blank=True)
    n_reformulacoes = models.IntegerField(null=True, blank=True, default=0)
    n_docs = models.CharField(max_length=40, null=True, blank=True)
    n_aviso_encerramento = models.CharField(max_length=40, null=True, blank=True)
    n_prestacao_contas = models.CharField(max_length=80, null=True, blank=True)
    subprograma = models.TextField(choices=SUBPROGRAMA, null=True, blank=True)
    geracao_projeto = models.IntegerField(null=False, blank=False)
    gestor_dateg = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING, related_name='usuario_projeto_gestor')

    #vigencia
    data_inicio = models.DateField()
    data_fim = models.DateField()

    #observacoes
    observacoes_gerais = models.TextField(null=True, blank=True, default='Sem observações.')

    #delete (del)
    del_status = models.BooleanField(default=False)
    del_data = models.DateTimeField(null=True, blank=True)
    del_usuario = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='usuario_projeto_deletado')

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
        super(Projetos, self).save(*args, **kwargs)


    def soft_delete(self, user):
        self.del_status = True
        self.del_data = timezone.now()
        self.del_usuario = user
        self.save()


    def __str__(self):
        return f"Projeto: {self.nome_plano_trabalho} (ID: {self.id}) - Regional: {self.regional}"


class ProjetosAtividadesProdutivas(models.Model):
    #relacionamento
    usuario_registro = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING, related_name='usuario_projeto_atividade_registro')
    usuario_atualizacao = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING, related_name='usuario_projeto_atividade_edicao')
    
    #log
    registro_data = models.DateTimeField(auto_now_add=True)
    ult_atual_data = models.DateTimeField(auto_now=True)
    log_n_edicoes = models.IntegerField(default=1)

    #atividade
    atividade = models.IntegerField(choices=ATIVIDADES_ATEG, null=False, blank=False)
    n_propriedades = models.IntegerField(null=False, blank=False, default=0)
    n_cadernos = models.IntegerField(null=False, blank=False, default=0)
    n_tecnicos = models.IntegerField(null=False, blank=False, default=0)
    n_supervisores = models.IntegerField(null=False, blank=False, default=0)
    n_tecnicos_supervisores_ead = models.IntegerField(null=False, blank=False, default=0)

    #projeto
    projeto = models.ForeignKey(Projetos, on_delete=models.DO_NOTHING, related_name='projeto_atividade_produtiva')

    #observacoes
    observacoes_gerais = models.TextField(null=True, blank=True, default='Sem observações.')

    #delete (del)
    del_status = models.BooleanField(default=False)
    del_data = models.DateTimeField(null=True, blank=True)
    del_usuario = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='usuario_projeto_atividade_deletado')

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
        super(ProjetosAtividadesProdutivas, self).save(*args, **kwargs)


    def soft_delete(self, user):
        self.del_status = True
        self.del_data = timezone.now()
        self.del_usuario = user
        self.save()


    def __str__(self):
        return f"Atividade: {self.atividade} (ID: {self.id}) - Projeto: {self.projeto.nome_plano_trabalho} ID SisATeG: {self.projeto.id_projeto_sisateg}"