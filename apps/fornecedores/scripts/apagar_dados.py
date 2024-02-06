from apps.fornecedores.models import CNPJ_CNAE

def run():
    # Apagar todos os registros
    CNPJ_CNAE.objects.all().delete()


#python manage.py runscript apps.fornecedores.scripts.apagar_dados