# Generated by Django 4.2.5 on 2023-11-20 23:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0007_alter_usuario_cad_unidade_daf_info'),
        ('produtos', '0018_alter_produtosfarmaceuticos_concentracao_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProdutoConsumoMedio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registro_data', models.DateTimeField(auto_now_add=True)),
                ('tipo_cmm', models.CharField(max_length=20)),
                ('data_referencia', models.DateField()),
                ('periodo_referencia', models.CharField(blank=True, max_length=10, null=True)),
                ('estoque_ses', models.FloatField()),
                ('aprovado_administrativo', models.FloatField()),
                ('aprovado_judicial', models.FloatField()),
                ('cmm_administrativo', models.FloatField()),
                ('cmm_judicial', models.FloatField()),
                ('cmm_total', models.FloatField()),
                ('observacoes', models.TextField(blank=True, default='Sem observações.', null=True)),
                ('responsavel_dados', models.CharField(max_length=20)),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='produto_cmm', to='produtos.produtosfarmaceuticos')),
                ('usuario_registro', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='usuario_registro_cmm', to='usuarios.usuario')),
            ],
        ),
    ]