import openpyxl
from django.utils import timezone
from apps.fornecedores.models import UF_Municipio

def import_from_excel(file_path):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    for row in sheet.iter_rows(min_row=2, values_only=True): 
        lista_uf_municipio = UF_Municipio()
        lista_uf_municipio.cod_ibge = row[0]
        lista_uf_municipio.uf_sigla = row[1]
        lista_uf_municipio.uf = row[2]
        lista_uf_municipio.municipio = row[3]
        lista_uf_municipio.municipio_uf = row[4]
        lista_uf_municipio.save()

def run():
    # Caminho do arquivo que você quer importar
    #file_path = r"C:\Users\alan.ribeiro\Desktop\SisDAF\dados\lista_uf_municipio.xlsx"
    file_path = 'dados/lista_uf_municipio.xlsx'
    import_from_excel(file_path)


#python manage.py runscript apps.fornecedores.scripts.import_lista_uf_municipio