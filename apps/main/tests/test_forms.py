from django.test import TestCase
from apps.main.forms import LoginForms, CadastroForms

class LoginFormTest(TestCase):

    def test_form_fields(self):
        form = LoginForms()

        # Verifica se os campos estão presentes no formulário
        self.assertIn('cpf', form.fields)
        self.assertIn('senha', form.fields)

        # Verifica se o campo CPF tem os atributos corretos
        self.assertEqual(form.fields['cpf'].label, "CPF")
        self.assertEqual(form.fields['cpf'].required, True)
        self.assertEqual(form.fields['cpf'].max_length, 14)
        self.assertEqual(form.fields['cpf'].widget.attrs['placeholder'], "Digite o seu CPF")
        self.assertEqual(form.fields['cpf'].widget.attrs['class'], "form-control")
        self.assertEqual(form.fields['cpf'].widget.attrs['id'], "cpf")

        # Verifica se o campo Senha tem os atributos corretos
        self.assertEqual(form.fields['senha'].label, "Senha")
        self.assertEqual(form.fields['senha'].required, True)
        self.assertEqual(form.fields['senha'].max_length, 50)
        self.assertEqual(form.fields['senha'].widget.attrs['placeholder'], "Digite a sua senha")
        self.assertEqual(form.fields['senha'].widget.attrs['class'], "form-control")

    def test_form_validation(self):
        # Caso válido
        form = LoginForms(data={
            'cpf': '999.944.401-50',
            'senha': 'password123'
        })
        self.assertTrue(form.is_valid())

        # Caso inválido (CPF vazio e senha com mais de 50 caracteres)
        form_invalid = LoginForms(data={
            'cpf': '',
            'senha': 'a' * 51
        })
        self.assertFalse(form_invalid.is_valid())
        self.assertIn('cpf', form_invalid.errors)
        self.assertIn('senha', form_invalid.errors)


class CadastroFormTest(TestCase):
    
    def test_form_fields(self):
        form = CadastroForms()

        #Verificar se os campos estão presentes no formulário
        self.assertIn('cpf', form.fields)
        self.assertIn('nome_usuario', form.fields)
        self.assertIn('email_ms', form.fields)
        self.assertIn('email_pessoal', form.fields)
        self.assertIn('celular', form.fields)
        self.assertIn('setor_daf', form.fields)
        self.assertIn('senha_1', form.fields)
        self.assertIn('senha_2', form.fields)
        
        #Verifica se o campo CPF tem os atributos corretos
        self.assertEqual(form.fields['cpf'].label, "CPF")
        self.assertEqual(form.fields['cpf'].required, True)
        self.assertEqual(form.fields['cpf'].max_length, 14)

        #Verifica se o campo nome_usuario tem os atributos corretos
        self.assertEqual(form.fields['nome_usuario'].label, "Nome Completo")
        self.assertEqual(form.fields['nome_usuario'].required, True)
        self.assertEqual(form.fields['nome_usuario'].max_length, 50)

        #Verifica se o campo email_ms tem os atributos corretos
        self.assertEqual(form.fields['email_ms'].label, "Email MS")
        self.assertEqual(form.fields['email_ms'].required, True)
        self.assertEqual(form.fields['email_ms'].max_length, 50)

        #Verifica se o campo email_pessoal tem os atributos corretos
        self.assertEqual(form.fields['email_pessoal'].label, "Email Pessoal")
        self.assertEqual(form.fields['email_pessoal'].required, True)
        self.assertEqual(form.fields['email_pessoal'].max_length, 50)

        #Verifica se o campo celular tem os atributos corretos
        self.assertEqual(form.fields['celular'].label, "Celular")
        self.assertEqual(form.fields['celular'].required, True)
        self.assertEqual(form.fields['celular'].max_length, 16)

        #Verifica se o campo setor_daf tem os atributos corretos
        self.assertEqual(form.fields['setor_daf'].label, "Unidade do DAF")
        self.assertEqual(form.fields['setor_daf'].required, True)

        #Verifica se o campo senha_1 tem os atributos corretos
        self.assertEqual(form.fields['senha_1'].label, "Senha")
        self.assertEqual(form.fields['senha_1'].required, True)
        self.assertEqual(form.fields['senha_1'].min_length, 6)
        self.assertEqual(form.fields['senha_1'].max_length, 50)

        #Verifica se o campo senha_2 tem os atributos corretos
        self.assertEqual(form.fields['senha_2'].label, "Confirme a Senha")
        self.assertEqual(form.fields['senha_2'].required, True)
        self.assertEqual(form.fields['senha_1'].min_length, 6)
        self.assertEqual(form.fields['senha_2'].max_length, 50)
        

    def test_form_validation(self):
        # Caso válido
        valid_data = {
            'cpf': '999.999.999-99',
            'nome_usuario': 'João da Silva Carvalho',
            'email_ms': 'joao.silva@saude.gov.br',
            'email_pessoal': 'joao.silva@gmail.com',
            'celular': '(99) 91234-5678',
            'setor_daf': 'gabinete',
            'senha_1': 'password123',
            'senha_2': 'password123',
        }
        form = CadastroForms(data=valid_data)
        self.assertTrue(form.is_valid())

        # Caso inválido
        invalid_data = valid_data.copy()
        invalid_data['cpf'] = '123'
        invalid_data['email_ms'] = 'email_invalido'
        invalid_data['senha_2'] = 'password1234'
        
        form_invalid = CadastroForms(data=invalid_data)
        self.assertFalse(form_invalid.is_valid())
        self.assertIn('email_ms', form_invalid.errors)
        self.assertNotEqual(form_invalid.cleaned_data['senha_1'], form_invalid.cleaned_data['senha_2'])