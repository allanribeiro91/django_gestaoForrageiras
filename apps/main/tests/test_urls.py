from django.test import TestCase, RequestFactory
from django.urls import reverse
from apps.main.views import login

class LoginURLSTestCase(TestCase):
    
    def setUp(self):
        self.factory = RequestFactory()

    def test_rota_url_utiliza_view_login(self):
        """Teste se a página de login utiliza a função login da view"""
        request = self.factory.get('/')
        with self.assertTemplateUsed('main/login.html'):
            response = login(request)
            self.assertEqual(response.status_code, 200)