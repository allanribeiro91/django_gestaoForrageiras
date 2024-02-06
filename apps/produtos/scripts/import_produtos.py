import openpyxl
from django.utils import timezone
from apps.produtos.models import ProdutosFarmaceuticos 

def import_from_excel(file_path):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    for row in sheet.iter_rows(min_row=2, values_only=True): 
        produto = ProdutosFarmaceuticos()

        produto.id = row[0]
        produto.usuario_registro_id = 1
        produto.usuario_atualizacao_id = 1
        produto.denominacao_id = row[3]

        #log
        produto.registro_data = timezone.now()
        produto.ult_atual_data = timezone.now()
        produto.log_n_edicoes = 1

        #dados do produto farmacêutico
        produto.produto = row[7]
        produto.concentracao_tipo = row[8]
        produto.concentracao = row[9]
        produto.forma_farmaceutica = row[10]
        produto.oncologico = row[11]
        produto.biologico = row[12]
        produto.aware = row[13]
        produto.atc = row[14]
        produto.atc_descricao = row[15]
        
        #incorporacao SUS
        produto.incorp_status = row[16]
        produto.incorp_data = row[17]
        produto.incorp_portaria = row[18]
        produto.incorp_link = row[19]
        produto.exclusao_data = row[20]
        produto.exclusao_portaria = row[21]
        produto.exclusao_link = row[22]

        #pactuacao
        produto.comp_basico = row[23]
        produto.comp_especializado = row[24]
        produto.comp_estrategico = row[25]

        #outros
        produto.disp_farmacia_popular = row[26]
        produto.hospitalar = row[27]
        
        #outros sistemas
        produto.sigtap_possui = row[28]
        produto.sigtap_codigo = row[29]
        produto.sigtap_nome = row[30]
        produto.sismat_possui = row[31]
        produto.sismat_codigo = row[32]
        produto.sismat_nome = row[33]
        produto.catmat_possui = row[34]
        produto.catmat_codigo = row[35]
        produto.catmat_nome = row[36]
        produto.obm_possui = row[37]
        produto.obm_codigo = row[38]
        produto.obm_nome = row[39]
        
        #observações gerais
        produto.observacoes_gerais = row[40]

        #delete (del)
        produto.del_status = row[41]
        produto.del_data = None if not row[42] else row[42]
        produto.del_usuario = None if not row[43] else row[43]
        
        produto.save()

def run():
    # Caminho do arquivo que você quer importar
    #file_path = r"G:\Meu Drive\Django\SisDAF\dados\produto_daf.xlsx"
    #file_path = r"C:\Users\aribe\OneDrive\Área de Trabalho\SisDAF\dados\produto_daf.xlsx"
    file_path = 'dados/produto_daf.xlsx'
    import_from_excel(file_path)


#python manage.py runscript apps.produtos.scripts.import_produtos