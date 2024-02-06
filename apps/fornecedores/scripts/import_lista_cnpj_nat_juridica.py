import openpyxl
from django.utils import timezone
from apps.fornecedores.models import CNPJ_NATUREZA_JURIDICA

def import_from_excel(file_path):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    for row in sheet.iter_rows(min_row=2, values_only=True): 
        lista_cnpj_nat_juridica = CNPJ_NATUREZA_JURIDICA()
        lista_cnpj_nat_juridica.codigo = row[0]
        lista_cnpj_nat_juridica.tipo = row[1]
        lista_cnpj_nat_juridica.natureza_juridica = row[2]
        lista_cnpj_nat_juridica.representante_entidade = row[3]
        lista_cnpj_nat_juridica.qualificacao = row[4]
        lista_cnpj_nat_juridica.save()

def run():
    # Caminho do arquivo que você quer importar
    #file_path = r"C:\Users\alan.ribeiro\Desktop\SisDAF\dados\lista_cnpj_natureza_juridica.xlsx"
    file_path = 'dados/lista_cnpj_natureza_juridica.xlsx'
    import_from_excel(file_path)


#python manage.py runscript apps.fornecedores.scripts.import_lista_cnpj_nat_juridica