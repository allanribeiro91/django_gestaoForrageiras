from apps.processos_aquisitivos.models import PROAQ_ETAPA

def run():
    # Apagar todos os registros
    PROAQ_ETAPA.objects.all().delete()

#python manage.py runscript apps.processos_aquisitivos.scripts.apagar_dados_proaq