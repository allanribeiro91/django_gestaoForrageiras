# Generated by Django 4.2.5 on 2023-11-14 21:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0007_alter_usuario_cad_unidade_daf_info'),
        ('fornecedores', '0017_alter_fornecedores_hierarquia_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fornecedores',
            name='porte',
            field=models.CharField(choices=[('me', 'ME'), ('medio_porte', 'Médio Porte'), ('demais', 'Demais'), ('epp', 'EPP'), ('grande_empresa', 'Grande Empresa'), ('mei', 'MEI')], max_length=20),
        ),
        migrations.AlterField(
            model_name='fornecedores',
            name='tipo_direito',
            field=models.CharField(choices=[('privado', 'Privado'), ('público', 'Público')], default='privado', max_length=10),
        ),
        migrations.CreateModel(
            name='Fornecedores_Comunicacoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registro_data', models.DateTimeField(auto_now_add=True)),
                ('ult_atual_data', models.DateTimeField(auto_now=True)),
                ('log_n_edicoes', models.IntegerField(default=1)),
                ('unidade_daf', models.CharField(choices=[('cgafb', 'CGAFB'), ('cgafme', 'CGAFME'), ('cgceaf', 'CGCEAF'), ('cgfp', 'CGFP'), ('cofisc', 'COFISC'), ('gabinete', 'GABINETE'), ('nao_informado', 'Não Informado')], max_length=15)),
                ('tipo_comunicacao', models.CharField(choices=[('email', 'Email'), ('oficio', 'Ofício'), ('ligacao_telefonica', 'Ligação Telefônica'), ('whatsapp', 'Whatsapp'), ('carta', 'Carta'), ('outro', 'Outro'), ('nao_informado', 'Não Informado')], max_length=25)),
                ('topico_comunicacao', models.CharField(blank=True, choices=[('contrato', 'Contrato'), ('entrega_produto', 'Entrega de Produto Farmacêutico'), ('nota_fiscal', 'Nota Fiscal'), ('pregao', 'Pregão Eletrônico'), ('processo_incorporacao', 'Processo de Incorporação'), ('outro', 'Outro')], max_length=40, null=True)),
                ('assunto', models.CharField(blank=True, max_length=200, null=True)),
                ('demanda_original', models.TextField(blank=True, null=True)),
                ('destinatario', models.TextField(blank=True, null=True)),
                ('mensagem_encaminhada', models.TextField(blank=True, null=True)),
                ('status_envio', models.CharField(blank=True, choices=[('nao_enviado', 'Não Enviado'), ('enviado', 'Enviado'), ('nao_informado', 'Não Informado')], max_length=40, null=True)),
                ('data_envio', models.DateField(blank=True, null=True)),
                ('outro_responsavel', models.CharField(blank=True, max_length=80, null=True)),
                ('observacoes_gerais', models.TextField(blank=True, default='Sem observações.', null=True)),
                ('del_status', models.BooleanField(default=False)),
                ('del_data', models.DateTimeField(blank=True, null=True)),
                ('del_usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='fornecedor_comunicacao_deletado', to='usuarios.usuario')),
                ('fornecedor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='fornecedor_comunicacao', to='fornecedores.fornecedores')),
                ('responsavel_resposta', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='fornecedor_comunicacao_responsavel', to='usuarios.usuario')),
                ('usuario_atualizacao', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='fornecedor_comunicacao_edicao', to='usuarios.usuario')),
                ('usuario_registro', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='fornecedor_comunicacao_registro', to='usuarios.usuario')),
            ],
        ),
    ]