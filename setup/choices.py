#Choices
YES_NO = [
    (True, 'Sim'),
    (False, 'Não'),
]

COR_PELE = [
    ('branco', 'Branco'),
    ('preto', 'Preto'),
    ('pardo', 'Pardo'),
    ('amarelo', 'Amarelo'),
    ('vermelho', 'Vermelho'),
    ('outro', 'Outro'),
    ('nao_informado', 'Não Informado'),
]

GENERO_SEXUAL = [
    ('masculino', 'Masculino'),
    ('feminino', 'Feminino'),
    ('outro', 'Outro'),
    ('nao_informado', 'Não Informado'),
]

UNIDADE = [
    ('', 'Não Informado'),
    ('dateg', "DATeG"),
    ('icna', "ICNA"),
]  

LOGS_ACAO = [
    ('create', "Create"),
    ('update', "Update"),
    ('delete', "Delete"),
]

STATUS_PROJETO = [
    ('', ''),
    ('em_elaboracao', "Em Elaboração"),
    ('em_execucao', "Em Execução"),
    ('finalizado', "Finalizado"),
    ('suspenso', "Suspenso"),
    ('cancelado', "Cancelado"),
]

LISTA_UFS_SIGLAS = [
    ('', ''),
    ('ac', 'AC'),
    ('al', 'AL'),
    ('am', 'AM'),
    ('ap', 'AP'),
    ('ba', 'BA'),
    ('ce', 'CE'),
    ('df', 'DF'),
    ('es', 'ES'),
    ('go', 'GO'),
    ('ma', 'MA'),
    ('mg', 'MG'),
    ('ms', 'MS'),
    ('mt', 'MT'),
    ('pa', 'PA'),
    ('pb', 'PB'),
    ('pe', 'PE'),
    ('pi', 'PI'),
    ('pr', 'PR'),
    ('rj', 'RJ'),
    ('rn', 'RN'),
    ('ro', 'RO'),
    ('rr', 'RR'),
    ('rs', 'RS'),
    ('sc', 'SC'),
    ('se', 'SE'),
    ('sp', 'SP'),
    ('to', 'TO'),
]

LISTA_ANOS = [
    (2018, 2018),
    (2019, 2019),
    (2020, 2020),
    (2021, 2021),
    (2022, 2022),
    (2023, 2023),
    (2024, 2024),
]

LISTA_TEXTURA_SOLO = [
    ('', ''),
    ('arenoso', 'Arenoso'),
    ('argiloso_arenoso', 'Argiloso/Arenoso'),
    ('argiloso', 'Argiloso'),
    ('muito_argiloso', 'Muito Argiloso'),
]

LISTA_MESES = [
    ('', ''),
    (1, 'Janeiro'),
    (2, 'Fevereiro'),
    (3, 'Março'),
    (4, 'Abril'),
    (5, 'Maio'),
    (6, 'Junho'),
    (7, 'Julho'),
    (8, 'Agosto'),
    (9, 'Setembro'),
    (10, 'Outubro'),
    (11, 'Novembro'),
    (12, 'Dezembro'),
]

ESPECIES_ANIMAIS = [
    ('', ''),
    ('ovinos', 'Ovino'),
    ('bovino_corte', 'Bovino de Corte'),
    ('bovino_leite', 'Bovino de Leite'),
]

ESPECIES_VEGETAIS = [
    ('', ''),
    ('cactaceas', 'Cactáceas'),
    ('gramineas_anuais', 'Gramíneas Anuais'),
    ('gramineas_perenes', 'Gramíneas Perenes'),
]

LOCAL_PREPARO_AMOSTRAS = [
    ('', ''),
    ('area_experimento', 'Área do Experimento'),
    ('sede', 'Sede'),
]








SUBPROGRAMA = [
    ('', ''),
    ('agronordeste2', 'Agronordeste 2'),
    ('cadeias_produtivas', 'Cadeias Produtivas'),
    ('expansao_ateg', 'Expansão ATeG'),
    ('expansao_ateg_2_1', 'Expansão ATeG 2-1'),
    ('especiais_diretoria', 'Especiais Diretoria'),
]

ATIVIDADES_ATEG = [
    ('', ''),
    (12, 'Agricultura Anual'),
    (15, 'Agricultura Orgânica'),
    (23, 'Agroindústria da Cana de Acúcar'),
    (37, 'Agroindústria de Azeite de Oliva'),
    (38, 'Agroindústria de Cera'),
    (25, 'Agroindústria de Derivados Lácteos'),
    (31, 'Agroindústria de Derivados Vegetais'),
    (35, 'Agroindústria de Farinha e Mandioca'),
    (41, 'Agroindústria de Ovos'),
    (36, 'Agroindústria de Panificação'),
    (33, 'Agroindústria de Pescado'),
    (34, 'Agroindústria de Polpas e Bebidas'),
    (39, 'Agroindústria de Produtos Apícola'),
    (26, 'Agroindústria de Embutidos, Defumados e Processo de Carnes'),
    (30, 'Agroindústria de Lácetos'),
    (8, 'Apicultura'),
    (10, 'Avicultura'),
    (2, 'Bovinocultura de Corte'),
    (1, 'Bovinocultura de Leite'),
    (14, 'Cacauicultura'),
    (3, 'Cafeicultura'),
    (20, 'Cana de Açúcar'),
    (19, 'Carcinicultura'),
    (28, 'Equideocultura'),
    (13, 'Floresta'),
    (17, 'Floricultura'),
    (4, 'Fruticultura Perene'),
    (27, 'Heveicultura'),
    (11, 'Maricultura'),
    (21, 'Minhocultura'),
    (7, 'Olericultura'),
    (6, 'Ovinocaprinocultura de Corte'),
    (5, 'Ovinocaprinocultura de Leite'),
    (29, 'Pipericultura'),
    (9, 'Piscicultura'),
    (42, 'Silvicultura'),
    (24, 'Sisalicultura'),
    (32, 'Sistemas Integrados de Produção'),
    (18, 'Suinocultura')
]

STATUS_CONTRATOS_TECNICOS = [
    ('em_elaboracao', 'Em elaboração'),
    ('em_analise', 'Em análise'),
    ('em_execucao', 'Em Execução'),
    ('finalizado', 'Finalizado'),
    ('suspenso', 'Suspenso'),
    ('cancelado', 'Cancelado'),
    ('nao_informado', 'Não Informado'),
]

FORMACAO_TECNICA = [
    ('agronomia', 'Agronomia'),
    ('medicina_veterinaria', 'Medicina Veterinária'),
    ('zootecnia', 'Zootecnia'),
    ('outro', 'Outro'),
    ('nao_informado', 'Não Informado'),
]










YES_NO = [
    (True, 'Sim'),
    (False, 'Não'),
]

COR_PELE = [
    ('branco', 'Branco'),
    ('preto', 'Preto'),
    ('pardo', 'Pardo'),
    ('amarelo', 'Amarelo'),
    ('vermelho', 'Vermelho'),
    ('outro', 'Outro'),
    ('nao_informado', 'Não Informado'),
]

GENERO_SEXUAL = [
    ('masculino', 'Masculino'),
    ('feminino', 'Feminino'),
    ('outro', 'Outro'),
    ('nao_informado', 'Não Informado'),
]


ORGAO_PUBLICO = [
    ('min_saude', "Ministério da Saúde"),
    ('outro', "Outro"),
    ('nao_informado', 'Não Informado'),
]





VINCULO_MS = [
    ('consultor', "Consultor Técnico"),
    ('servidor_federal', "Servidor Federal"),
    ('servidor_estadual', "Servidor Estadual"),
    ('servidor_municipal', "Servidor Municipal"),
    ('nao_informado', 'Não Informado'),
]



LOGS_ACAO = [
    ('create', "Create"),
    ('update', "Update"),
    ('delete', "Delete"),
]

MODALIDADE_AQUISICAO = [
    ('emergencial', "Emergencial"),
    ('inexigibilidade', "Inexigibilidade"),
    ('pregao_comarp', "Pregão Com ARP"),
    ('pregao_semarp', "Pregão Sem ARP"),
]




STATUS_SISDAF = [
    ('ativo', "Ativo"),
    ('inativo', "Inativo"),
    ('em_desenvolvimento', "Em Desenvolvimento"),
]


LEI_LICITACAO = [
    ('lei_8666', "Lei 8.666/93"),
    ('lei_14133', "Lei 14.133/21"),
    ('nao_informado', "Não Informado"),
]

CNPJ_HIERARQUIA = {
    ('matriz', 'Matriz'),
    ('filial', 'Filial'),
}

CNPJ_PORTE = {
    ('mei', 'MEI'),
    ('me', 'ME'),
    ('epp', 'EPP'),
    ('medio_porte', 'Médio Porte'),
    ('grande_empresa', 'Grande Empresa'),
    ('demais', 'Demais'),
}

TIPO_DIREITO = {
    ('privado', 'Privado'),
    ('público', 'Público'),
}

TIPO_COTA = [
    ('principal', 'Principal'),
    ('reservada', 'Reservada'),
]

FAQ_FORNECEDOR_TOPICO = [
    ('contrato', 'Contrato'),
    ('entrega_produto','Entrega de Produto Farmacêutico'),
    ('nota_fiscal','Nota Fiscal'),
    ('pregao','Pregão Eletrônico'),
    ('processo_incorporacao','Processo de Incorporação'),
    ('outro','Outro'),
]

CARGOS_FUNCOES = [
    ('representante_comercial','Representante Comercial'),
    ('assessor_tecnico', 'Assessor Técnico'),
    ('gerente','Gerente'),
    ('coordenador','Coordenador'),
    ('diretor','Diretor'),
    ('vice_presidente','Vice-Presidente'),
    ('presidente','Presidente'),
    ('outro','Outro'),
    ('nao_informado','Não Informado'),
]

TIPO_COMUNICACAO = [
    ('email','Email'),
    ('oficio','Ofício'),
    ('ligacao_telefonica','Ligação Telefônica'),
    ('whatsapp','Whatsapp'),
    ('carta', 'Carta'),
    ('outro','Outro'),
    ('nao_informado','Não Informado'),
]

STATUS_ENVIO_COMUNICACAO = [
    ('nao_enviado','Não Enviado'),
    ('enviado','Enviado'),
    ('nao_informado','Não Informado'),
]

LISTA_TRIMESTRES = [
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
]

FONTES_CONTRATOS_CONSULTORES = [
    ('fiotec', 'FIOTEC'),
    ('opas', 'OPAS'),
    ('outro', 'Outro'),
    ('', 'Não Informado'),
]



INSTRUMENTOS_JURIDICOS_CONSULTORES = [
    ('TC132', 'TC132'),
    ('', 'Não Informado'),
]