from apps.produtos.models import ProdutosFarmaceuticos

def set_fields_to_false():
    ProdutosFarmaceuticos.objects.update(
        sigtap_possui=True,
        sismat_possui=True,
        catmat_possui=True,
        obm_possui=True
    )

def run():
    set_fields_to_false()

#python manage.py runscript apps.produtos.scripts.produtos_atualizar