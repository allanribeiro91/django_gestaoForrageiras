import openpyxl
from django.utils import timezone
from apps.processos_aquisitivos.models import PROAQ_AREA_MS

def import_from_excel(file_path):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    for row in sheet.iter_rows(min_row=2, values_only=True): 
        lista_area_ms = PROAQ_AREA_MS()
        lista_area_ms.setor = row[0]
        lista_area_ms.orgao_publico = row[1]
        lista_area_ms.ministerio = row[2]
        lista_area_ms.secretaria = row[3]
        lista_area_ms.departamento = row[4]
        lista_area_ms.save()

def run():
    # Caminho do arquivo que você quer importar
    #file_path = r"C:\Users\alan.ribeiro\Desktop\SisDAF\dados\proaq_area_ms.xlsx"
    file_path = 'dados/proaq_area_ms.xlsx'
    import_from_excel(file_path)

#python manage.py runscript apps.processos_aquisitivos.scripts.import_lista_area_ms