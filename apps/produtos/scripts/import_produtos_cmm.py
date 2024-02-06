import openpyxl
from django.utils import timezone
from apps.produtos.models import ProdutoConsumoMedio 


def import_from_excel(file_path):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    for row in sheet.iter_rows(min_row=2, values_only=True): 
        item = ProdutoConsumoMedio()
        # item.id = row[0]
        item.usuario_registro_id = 1
        item.registro_data = timezone.now()
        item.tipo_cmm = row[2]
        item.data_referencia = row[3]
        item.periodo_referencia = row[4]
        item.produto_id = row[5]
        item.estoque_ses = row[6]
        item.aprovado_administrativo = row[7]
        item.aprovado_judicial = row[8]
        item.aprovado_total = row[9]
        item.cmm_administrativo = row[10]
        item.cmm_judicial = row[11]
        item.cmm_total = row[12]
        item.observacoes = row[13]
        item.responsavel_dados = row[14]
        item.save()

def run():
    # Caminho do arquivo que você quer importar
    file_path = 'dados/produto_daf_cmm.xlsx'
    import_from_excel(file_path)

#python manage.py runscript apps.produtos.scripts.import_produtos_cmm