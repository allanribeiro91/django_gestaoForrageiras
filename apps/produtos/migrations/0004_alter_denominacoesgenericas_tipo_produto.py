# Generated by Django 4.2.5 on 2023-09-12 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0003_denominacoesgenericas_log_n_edicoes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='denominacoesgenericas',
            name='tipo_produto',
            field=models.CharField(blank=True, choices=[('Insumo', 'Insumo'), ('Medicamento', 'Medicamento'), ('nao_informado', 'Não Informado')], max_length=15, null=True),
        ),
    ]