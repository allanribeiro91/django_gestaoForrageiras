from django.test import LiveServerTestCase
from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
#from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class CadastroTestCase(LiveServerTestCase):
    """Verificar se o cadastro está funcionando corretamente."""

    def setUp(self):
        #service = Service(ChromeDriverManager().install())
        #self.browser = webdriver.Chrome(service=service)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("webdriver.chrome.driver=chromedriver.exe")
        self.browser = webdriver.Chrome(options=chrome_options)
        
    def tearDown(self):
        self.browser.quit()

    def test_cadastro_usuario_sisdaf(self):
        """Testar se existe o botão 'Cadastrar' na página de Login do SisDAF."""
        
        #Usuário acessa a página inicial do SisDAF
        self.browser.get(self.live_server_url + '/')
        
        #Buscar o elemento 'Cadastrar' pelo ID
        try:
            link_cadastrar = self.browser.find_element(By.ID, "cadastrar")
        except NoSuchElementException:
            self.fail("Elemento com ID 'cadastrar' não foi encontrado na página.")
        
        #Verificações do elemento 'Cadastrar'
        self.assertTrue(link_cadastrar.is_displayed(), "Link 'Cadastrar' não está visível.")
        self.assertTrue(link_cadastrar.is_enabled(), "Link 'Cadastrar' não está habilitado.")
        self.assertEqual(link_cadastrar.tag_name, 'a', "O elemento não é um link.")
        self.assertTrue(link_cadastrar.get_attribute('href'), "O link não possui um atributo href.")
        self.assertEqual(link_cadastrar.text, 'Cadastrar')
        
    