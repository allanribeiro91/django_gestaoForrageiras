from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.contrib.auth.models import User
from apps.usuarios.models import Usuarios
from apps.main.models import CustomLog
from setup.choices import LISTA_UFS_SIGLAS, LISTA_TRIMESTRES, LISTA_ANOS
from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string
from xhtml2pdf import pisa
from openpyxl import Workbook
from openpyxl.utils import get_column_letter
from datetime import datetime
from io import BytesIO
import json

@login_required
def prog_basico(request):
    # produtos = ProdutosFarmaceuticos.objects.filter(del_status=False).order_by('produto')
    # numero_produtos = produtos.count()
    # produtos = produtos[:100]

    conteudo = {
        # 'produtos': produtos,
        # 'TIPO_PRODUTO': TIPO_PRODUTO,
        # 'numero_produtos': numero_produtos,
    }
    return render(request, 'programacao/prog_basico.html', conteudo)




#COMPONENTE ESPECIALIZADO
@login_required
def prog_especializado(request):
    conteudo = {
        'lista_ses': LISTA_UFS_SIGLAS,
        'lista_trimestres': LISTA_TRIMESTRES,
        'lista_anos': LISTA_ANOS,
        'total_programacoes': 0,
    }
    return render(request, 'programacao/prog_especializado.html', conteudo)


def prog_especializado_ficha_prog(request):
    return render(request, 'programacao/prog_especializado_fase1.html')




@login_required
def prog_estrategico(request):
    # produtos = ProdutosFarmaceuticos.objects.filter(del_status=False).order_by('produto')
    # numero_produtos = produtos.count()
    # produtos = produtos[:100]

    conteudo = {
        # 'produtos': produtos,
        # 'TIPO_PRODUTO': TIPO_PRODUTO,
        # 'numero_produtos': numero_produtos,
    }
    return render(request, 'programacao/prog_estrategico.html', conteudo)