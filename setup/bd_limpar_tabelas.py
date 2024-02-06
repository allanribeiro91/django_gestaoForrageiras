from apps.fornecedores.models import Fornecedores_Faq, Fornecedores_Representantes, Fornecedores
from apps.processos_aquisitivos.models import ProaqDadosGerais, ProaqProdutos, ProaqEvolucao, ProaqTramitacao
from apps.produtos.models import DenominacoesGenericas, ProdutosFarmaceuticos, Tags, ProdutosTags
from apps.usuarios.models import Usuario, Alocacao

def run():
    #FORNECEDORES
    Fornecedores_Faq.objects.all().delete()
    Fornecedores_Representantes.objects.all().delete()
    
    # #PROCESSOS AQUISITIVOS
    ProaqProdutos.objects.all().delete()
    ProaqEvolucao.objects.all().delete()
    ProaqTramitacao.objects.all().delete()
    ProaqDadosGerais.objects.all().delete()

    # #PRODUTOS
    ProdutosTags.objects.all().delete()
    Tags.objects.all().delete()
    ProdutosFarmaceuticos.objects.all().delete()
    DenominacoesGenericas.objects.all().delete()

    #USUARIOS
    #Usuario.objects.all().delete()
    #Alocacao.objects.all().delete()


#python manage.py runscript setup.bd_limpar_tabelas