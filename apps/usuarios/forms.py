from django import forms
from django.core.exceptions import ValidationError
from apps.usuarios.models import Usuarios, Alocacoes
from datetime import datetime

class UsuarioForms(forms.ModelForm):
    class Meta:
        model = Usuarios
        exclude = ['user', 'data_registro', 'data_ultima_atualizacao', 'usuario_is_ativo', 'del_status', 'del_data', 'del_cpf']
        widgets = {
            #dados pessoais
            'cpf': forms.TextInput(attrs={'class':'form-control'}),
            'nome_completo': forms.TextInput(attrs={'class':'form-control'}),
            'data_nascimento': forms.DateInput(
                format='%d/%m/%Y',
                attrs={
                    'type': 'date',
                    'class':'form-control'}),
            'genero': forms.Select(attrs={
                'class':'form-control'
                }),
            'cor_pele': forms.Select(attrs={'class':'form-control'}),

            #foto
            'foto_usuario': forms.FileInput(attrs={'class':'form-control'}),

            #contato (ctt)
            'ramal_ms': forms.TextInput(attrs={'class':'form-control'}),
            'celular': forms.TextInput(attrs={'class':'form-control'}),
            'email_ms': forms.EmailInput(attrs={'class':'form-control'}),
            'email_pessoal': forms.EmailInput(attrs={'class':'form-control'}),

            #redes sociais (rs)
            'linkedin': forms.URLInput(attrs={'class':'form-control'}),
            'lattes': forms.URLInput(attrs={'class':'form-control'}),

        }


class AlocacaoForm(forms.ModelForm):

    class Meta:
        model = Alocacoes
        fields = ['unidade', 'setor', 'data_inicio', 'data_fim', 'is_ativo',
                  'del_status', 'del_data', 'del_cpf',
                  ]

    def clean_aloc_data_inicio(self):
        data = self.cleaned_data.get('aloc_data_inicio')
        if data:
            try:
                return datetime.strptime(data, '%d/%m/%Y').date()
            except ValueError:
                raise forms.ValidationError("Formato de data inválido. Use DD/MM/YYYY.")
        return data

    def clean(self):
        cleaned_data = super().clean()
        is_ativo = cleaned_data.get('is_ativo')
        data_fim = cleaned_data.get('data_fim')
        usuario = self.instance.usuario

        # Verifica se já existe uma alocação ativa para o usuário
        if is_ativo:
            alocacoes_ativas = Alocacoes.objects.filter(usuario=usuario, is_ativo=True).exclude(pk=self.instance.pk)
            if alocacoes_ativas.exists():
                raise ValidationError('Já existe uma alocação ativa para este usuário.')

        # Verifica se a data_fim está preenchida quando is_ativo é False
        if not is_ativo and data_fim is None:
            raise ValidationError('A data de fim é requerida quando a alocação não está ativa.')

        return cleaned_data

