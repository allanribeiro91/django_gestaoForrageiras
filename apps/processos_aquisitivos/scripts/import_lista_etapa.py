import openpyxl
from django.utils import timezone
from apps.processos_aquisitivos.models import PROAQ_ETAPA

def import_from_excel(file_path):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    for row in sheet.iter_rows(min_row=2, values_only=True): 
        lista_etapa = PROAQ_ETAPA()
        lista_etapa.etapa = row[0]
        lista_etapa.save()

def run():
    # Caminho do arquivo que você quer importar
    #file_path = r"C:\Users\alan.ribeiro\Desktop\SisDAF\dados\proaq_etapa_processo.xlsx"
    file_path = 'dados/proaq_etapa_processo.xlsx'
    import_from_excel(file_path)


#python manage.py runscript apps.processos_aquisitivos.scripts.import_lista_etapa