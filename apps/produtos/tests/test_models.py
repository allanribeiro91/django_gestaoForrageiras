from django.test import TestCase

class ProdutoTestCase(TestCase):
    
    def test_um_e_um(self):
        self.assertEqual(1,1)
