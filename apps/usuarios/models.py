from django.core.exceptions import ValidationError
from django.db import models
from datetime import date
from django.contrib.auth.models import User
from setup.choices import GENERO_SEXUAL, COR_PELE, UNIDADE

class Usuarios(models.Model):
    #relacionamento
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='usuario_relacionado')
    
    #log
    data_registro = models.DateTimeField(auto_now_add=True)
    data_ultima_atualizacao = models.DateTimeField(auto_now=True)
    
    #dados pessoais (dp)
    cpf = models.CharField(max_length=14, null=False, blank=False, unique=True)
    nome_completo = models.CharField(max_length=100, null=False, blank=False)
    data_nascimento = models.DateField(null=True, blank=True)
    genero = models.CharField(max_length=15, choices=GENERO_SEXUAL, null=True, blank=True)
    cor_pele = models.CharField(max_length=15, choices=COR_PELE, null=True, blank=True)

    #foto
    foto_usuario = models.ImageField(upload_to="fotos_usuarios/%Y/%m/%d/", blank=True)

    #contato (ctt)
    ramal = models.CharField(max_length=4, null=True, blank=True)
    celular = models.CharField(max_length=17, null=True, blank=True)
    email_institucional = models.EmailField(max_length=40, null=True, blank=True)
    email_pessoal = models.EmailField(max_length=40, null=True, blank=True)

    #redes sociais (rs)
    linkedin = models.URLField(max_length=150, null=True, blank=True)
    lattes = models.URLField(max_length=150, null=True, blank=True)

    #usuario está ativo
    usuario_is_ativo = models.BooleanField(default=True, null=False, blank=False, db_index=True)

    #delete (del)
    del_status = models.BooleanField(default=False)
    del_data = models.DateTimeField(null=True, blank=True)
    del_cpf = models.CharField(max_length=14, null=True, blank=True)

    def __str__(self):
        return f"{self.primeiro_ultimo_nome()}"
    
    def primeiro_ultimo_nome(self):
        partes_nome = self.nome_completo.split()
        primeiro_nome = partes_nome[0]
        ultimo_nome = partes_nome[-1] if len(partes_nome) > 1 else ''
        return f"{primeiro_nome} {ultimo_nome}"

    def alocacao_ativa(self):
        return self.alocacao.filter(is_ativo=True).first()

class Alocacoes(models.Model):
    # relacionamento
    usuario = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING, related_name='alocacao', null=True)
    
    # log
    data_registro = models.DateTimeField(auto_now_add=True)
    data_ultima_atualizacao = models.DateTimeField(auto_now=True)

    # alocacao atual
    unidade = models.CharField(max_length=20, choices=UNIDADE, null=False, blank=False)
    setor = models.CharField(max_length=60, null=True, blank=True)
    data_inicio = models.DateField(default=date.today, null=False, blank=False)
    data_fim = models.DateField(null=True, blank=True)
    is_ativo = models.BooleanField(default=True, null=False, blank=False, db_index=True)

    # delete (del)
    del_status = models.BooleanField(default=False)
    del_data = models.DateTimeField(null=True, blank=True)
    del_cpf = models.CharField(max_length=14, null=True, blank=True)

    def save(self, *args, **kwargs):
        # Verifica se já existe uma alocação ativa para o usuário
        if self.is_ativo:
            alocacoes_ativas = Alocacoes.objects.filter(usuario=self.usuario, is_ativo=True).exclude(pk=self.pk)
            if alocacoes_ativas.exists():
                raise ValidationError('Já existe uma alocação ativa para este usuário.')

        # Verifica se a data_fim está preenchida quando is_ativo é False
        if not self.is_ativo and self.data_fim is None:
            raise ValidationError('A data de fim é requerida quando a alocação não está ativa.')

        super(Alocacoes, self).save(*args, **kwargs)  # Chamando o save original

    def __str__(self):
        return f"Usuário: {self.usuario.nome_completo} ({self.usuario.cpf}) | Alocação: ({self.setor})"
