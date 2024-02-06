import openpyxl
from django.utils import timezone
from apps.produtos.models import Tags 


def import_from_excel(file_path):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    for row in sheet.iter_rows(min_row=2, values_only=True): 
        tags = Tags()
        tags.id = row[0]
        tags.tag = row[1]
        tags.save()

def run():
    # Caminho do arquivo que você quer importar
    #file_path = r"G:\Meu Drive\Django\SisDAF\dados\tags_produtos.xlsx"
    #file_path = r"C:\Users\aribe\OneDrive\Área de Trabalho\SisDAF\dados\tags_produtos.xlsx"
    file_path = 'dados/tags_produtos.xlsx'
    import_from_excel(file_path)

#python manage.py runscript apps.produtos.scripts.import_tags_produtos