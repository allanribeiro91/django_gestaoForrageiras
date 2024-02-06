from django.db import models
from apps.usuarios.models import Usuarios
from setup.choices import STATUS_SISDAF
from django.utils import timezone

class VersoesSisdaf(models.Model):
    #relacionamento
    usuario_registro = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING, related_name='versao_registro')
    usuario_atualizacao = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING, related_name='versao_edicao')
    
    #log
    registro_data = models.DateTimeField(auto_now_add=True)
    ult_atual_data = models.DateTimeField(auto_now=True)
    log_n_edicoes = models.IntegerField(default=1)

    #sobre a versao
    versao = models.TextField(max_length=15, null=False, blank=False)
    status = models.TextField(max_length=20, choices=STATUS_SISDAF, null=False, blank=False)
    data_versao = models.DateField(null=True, blank=True)
    informacoes = models.TextField(null=True, blank=True)

    #delete (del)
    del_status = models.BooleanField(default=False)
    del_data = models.DateTimeField(null=True, blank=True)
    del_usuario = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='versao_deletada')

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
        super(VersoesSisdaf, self).save(*args, **kwargs)


    def soft_delete(self, user):
        self.del_status = True
        self.del_data = timezone.now()
        self.del_usuario = user
        self.save()
