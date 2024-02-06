from django.db import models
from apps.usuarios.models import Usuarios
from setup.choices import LOGS_ACAO


class CustomLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING, related_name='log_usuario')
    modulo = models.CharField(max_length=140, null=False, blank=False)
    model = models.CharField(max_length=60, null=False, blank=False, default='Não informado')
    model_id = models.IntegerField(null=False, blank=False, default=0)
    item_id = models.IntegerField(null=False, blank=False)
    item_descricao = models.CharField(max_length=140, null=False, blank=False)
    acao = models.CharField(max_length=40, choices=LOGS_ACAO, null=False, blank=False)
    observacoes = models.CharField(max_length=240, default='Sem observações.', null=False, blank=False)

    def __str__(self):
        return f"{self.usuario} - {self.observacoes} em {self.timestamp}"

class UserAccessLog(models.Model):
    usuario = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING, related_name='acesso_usuario')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario} acessou em {self.timestamp}"