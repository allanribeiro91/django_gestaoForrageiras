import openpyxl
from django.utils import timezone
from apps.fornecedores.models import CNPJ_CNAE


def import_from_excel(file_path):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    for row in sheet.iter_rows(min_row=2, values_only=True): 
        lista_cnpj_cnae = CNPJ_CNAE()
        lista_cnpj_cnae.codigo = row[0]
        lista_cnpj_cnae.secao_codigo = row[1]
        lista_cnpj_cnae.secao_descricao = row[2]
        lista_cnpj_cnae.divisao_codigo = row[3]
        lista_cnpj_cnae.divisao_descricao = row[4]
        lista_cnpj_cnae.grupo_codigo = row[5]
        lista_cnpj_cnae.grupo_descricao = row[6]
        lista_cnpj_cnae.classe_codigo = row[7]
        lista_cnpj_cnae.classe_descricao = row[8]
        lista_cnpj_cnae.subclasse_codigo = row[9]
        lista_cnpj_cnae.subclasse_descricao = row[10]
        lista_cnpj_cnae.save()

def run():
    # Caminho do arquivo que você quer importar
    # file_path = r"C:\Users\alan.ribeiro\Desktop\SisDAF\dados\lista_cnpj_cnae.xlsx"
    file_path = 'dados/lista_cnpj_cnae.xlsx'
    import_from_excel(file_path)


#python manage.py runscript apps.fornecedores.scripts.import_lista_cnpj_cnae