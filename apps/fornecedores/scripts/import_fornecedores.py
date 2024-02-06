import openpyxl
from django.utils import timezone
from apps.fornecedores.models import Fornecedores

def import_from_excel(file_path):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    for row in sheet.iter_rows(min_row=2, values_only=True): 
        fornecedores = Fornecedores()
        #usuario
        fornecedores.usuario_registro_id = 1
        fornecedores.usuario_atualizacao_id = 1
        #log
        fornecedores.registro_data = timezone.now()
        fornecedores.ult_atual_data = timezone.now()
        fornecedores.log_n_edicoes = 1
        #dados do fornecedor
        fornecedores.cnpj = row[5]
        fornecedores.razao_social = row[6]
        fornecedores.nome_fantasia = row[7]
        fornecedores.hierarquia = row[8]
        fornecedores.porte = row[9]
        fornecedores.tipo_direito = row[10]
        fornecedores.data_abertura = row[11]
        fornecedores.natjuridica_codigo = row[12]
        fornecedores.natjuridica_descricao = row[13]
        #atividade empresarial
        fornecedores.ativ_principal_cod = row[14]
        fornecedores.ativ_principal_descricao = row[15]
        #endereco
        fornecedores.end_cep = row[16]
        fornecedores.end_uf = row[17]
        fornecedores.end_municipio = row[18]
        fornecedores.end_logradouro = row[19]
        fornecedores.end_numero = row[20]
        fornecedores.end_bairro = row[21]
        #observações gerais
        fornecedores.observacoes_gerais = row[22]
        #delete (del)
        fornecedores.del_status = row[23]

        #salvar
        fornecedores.save()

def run():
    # Caminho do arquivo que você quer importar
    #file_path = r"C:\Users\alan.ribeiro\Desktop\SisDAF\dados\fornecedores.xlsx"
    #file_path = r"C:\Users\aribe\OneDrive\Área de Trabalho\SisDAF\dados\fornecedores.xlsx"
    file_path = 'dados/fornecedores.xlsx'
    import_from_excel(file_path)


#python manage.py runscript apps.fornecedores.scripts.import_fornecedores