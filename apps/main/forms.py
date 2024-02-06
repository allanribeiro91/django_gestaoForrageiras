from django import forms
from setup.funcoes import valida_cpf


class LoginForms(forms.Form):
    cpf=forms.CharField(
        label="CPF",
        required=True,
        max_length=14,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite o seu CPF",
                "id": "cpf"
            }
        )
    )
    senha=forms.CharField(
        label="Senha",
        required=True,
        max_length=50,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite a sua senha"
            }
        )
    )

    

class CadastroForms(forms.Form):
    cpf=forms.CharField(
        label="CPF",
        required=True,
        max_length=14,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite o seu CPF",
                "id": "cpf"
            }
        )
    )
    nome_usuario=forms.CharField(
        label="Nome Completo",
        required=True,
        min_length=10,
        max_length=50, 
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite o seu nome completo",
            }
        )
    )
    email_institucional=forms.EmailField(
        label="Email Institucional",
        required=True,
        min_length=10,
        max_length=50, 
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite o seu email institucional",
                "id": "email_institucional"
            }
        )
    )
    email_pessoal=forms.EmailField(
        label="Email Pessoal",
        required=True,
        min_length=10,
        max_length=50, 
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                'id': 'email_pessoal',
                "placeholder": "Digite o seu email pessoal",
            }
        )
    )
    celular=forms.CharField(
        label="Celular",
        required=True,
        max_length=16,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": 'Digite o seu celular',
                "id": "celular",
            }
        )
    )
    senha_1=forms.CharField(
        label="Senha",
        required=True,
        min_length=6,
        max_length=50,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                'id': 'senha1',
                "placeholder": "Digite a senha",
                "autocomplete": "new-password"
            }
        )
    )
    senha_2=forms.CharField(
        label="Confirme a Senha",
        required=True,
        min_length=6,
        max_length=50,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                'id': 'senha2',
                "placeholder": "Digite a senha novamente",
                "autocomplete": "new-password"
            }
        )
    )

    