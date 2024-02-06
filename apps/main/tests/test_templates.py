from django.urls import reverse
from django.test import TestCase
from selenium.common.exceptions import NoSuchElementException


class LoginTemplateTests(TestCase):

    def setUp(self):
        # Você pode criar aqui algum usuário ou qualquer dado necessário 
        # para que o template de login seja renderizado corretamente.
        pass

    def test_login_template_used(self):
        response = self.client.get(reverse('login'))
        self.assertTemplateUsed(response, 'main/login.html')

    def test_login_elements_displayed(self):
        response = self.client.get(reverse('login'))
        # Verificar se os elementos chave estão presentes
        self.assertContains(response, 'SisDAF')
        self.assertContains(response, 'CPF')
        self.assertContains(response, 'Senha')
        self.assertContains(response, 'Esqueci a senha')
        self.assertContains(response, '<button type="submit">Entrar</button>')


    
