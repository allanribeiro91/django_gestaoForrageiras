import openpyxl
from django.utils import timezone
from apps.produtos.models import ListaATC 


def import_from_excel(file_path):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    for row in sheet.iter_rows(min_row=2, values_only=True): 
        lista_atc = ListaATC()
        lista_atc.id = row[0]
        lista_atc.codigo = row[1]
        lista_atc.nivel = row[2]
        lista_atc.descricao = row[3]
        lista_atc.save()

def run():
    # Caminho do arquivo que você quer importar
    #file_path = r"G:\Meu Drive\Django\SisDAF\dados\lista_atc.xlsx"
    file_path = 'dados/lista_atc.xlsx'
    import_from_excel(file_path)

#python manage.py runscript apps.produtos.scripts.import_lista_atc