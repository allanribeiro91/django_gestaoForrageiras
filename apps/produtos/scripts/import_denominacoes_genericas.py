import openpyxl
from django.utils import timezone
from apps.produtos.models import DenominacoesGenericas 
from apps.usuarios.models import Usuario 


def import_from_excel(file_path):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    for row in sheet.iter_rows(min_row=2, values_only=True): 
        denominacao = DenominacoesGenericas()

        denominacao.id = row[0]
        denominacao.usuario_registro_id = 1  
        denominacao.usuario_atualizacao_id = 1  
        denominacao.registro_data = timezone.now() 
        denominacao.ult_atual_data = timezone.now()
        denominacao.denominacao = row[5]
        denominacao.tipo_produto = row[6]
        denominacao.unidade_basico = row[7]
        denominacao.unidade_especializado = row[8]
        denominacao.unidade_estrategico = row[9]
        denominacao.unidade_farm_popular = row[10]
        denominacao.hospitalar = row[11]
        denominacao.observacoes_gerais = row[12]
        denominacao.del_status = row[13]
        denominacao.del_data = None if not row[14] else row[14]
        denominacao.del_cpf = None if not row[15] else row[15]
        
        denominacao.save()

def run():
    # Caminho do arquivo que você quer importar
    #file_path = r"G:\Meu Drive\Django\SisDAF\dados\DIM_DENOMINACAO_GENERICA.xlsx"
    #file_path = r"C:\Users\aribe\OneDrive\Área de Trabalho\SisDAF\dados\dim_denominacao_generica.xlsx"
    file_path = 'dados/dim_denominacao_generica.xlsx'
    import_from_excel(file_path)

#python manage.py runscript apps.produtos.scripts.import_denominacoes_genericas