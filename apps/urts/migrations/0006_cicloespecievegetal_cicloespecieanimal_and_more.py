# Generated by Django 4.2.5 on 2024-06-18 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
        ('urts', '0005_remove_cicloespeciesvegetaisanimais_ciclo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CicloEspecieVegetal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registro_data', models.DateTimeField(auto_now_add=True)),
                ('ult_atual_data', models.DateTimeField(auto_now=True)),
                ('log_n_edicoes', models.IntegerField(default=1)),
                ('especie_vegetal', models.CharField(blank=True, choices=[('', ''), ('cactaceas', 'Cactáceas'), ('gramineas_anuais', 'Gramíneas Anuais'), ('gramineas_perenes', 'Gramíneas Perenes')], max_length=140, null=True)),
                ('variedades', models.CharField(blank=True, max_length=140, null=True)),
                ('area_utilizada', models.FloatField(blank=True, default=0, null=True)),
                ('producao_silagem', models.BooleanField(blank=True, null=True)),
                ('observacoes_gerais', models.TextField(blank=True, default='Sem observações.', null=True)),
                ('del_status', models.BooleanField(default=False)),
                ('del_data', models.DateTimeField(blank=True, null=True)),
                ('ciclo', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='ciclo_especie_vegetal', to='urts.ciclo')),
                ('del_usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='usuario_ciclo_especie_vegetal_deletado', to='usuarios.usuarios')),
                ('urt', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='urt_ciclo_especie_vegetal', to='urts.urts')),
                ('usuario_atualizacao', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='usuario_ciclo_especie_vegetal_edicao', to='usuarios.usuarios')),
                ('usuario_registro', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='usuario_ciclo_especie_vegetal_registro', to='usuarios.usuarios')),
            ],
        ),
        migrations.CreateModel(
            name='CicloEspecieAnimal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registro_data', models.DateTimeField(auto_now_add=True)),
                ('ult_atual_data', models.DateTimeField(auto_now=True)),
                ('log_n_edicoes', models.IntegerField(default=1)),
                ('especie_animal', models.CharField(choices=[('', ''), ('ovinos', 'Ovino'), ('bovino_corte', 'Bovino de Corte'), ('bovino_leite', 'Bovino de Leite')], max_length=140)),
                ('racas', models.CharField(blank=True, max_length=140, null=True)),
                ('area_utilizada', models.FloatField(blank=True, default=0, null=True)),
                ('observacoes_gerais', models.TextField(blank=True, default='Sem observações.', null=True)),
                ('del_status', models.BooleanField(default=False)),
                ('del_data', models.DateTimeField(blank=True, null=True)),
                ('ciclo', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='ciclo_especie_animal', to='urts.ciclo')),
                ('del_usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='usuario_ciclo_especie_animal_deletado', to='usuarios.usuarios')),
                ('urt', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='urt_ciclo_especie_animal', to='urts.urts')),
                ('usuario_atualizacao', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='usuario_ciclo_especie_animal_edicao', to='usuarios.usuarios')),
                ('usuario_registro', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='usuario_ciclo_especie_animal_registro', to='usuarios.usuarios')),
            ],
        ),
        migrations.CreateModel(
            name='CicloAtividades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registro_data', models.DateTimeField(auto_now_add=True)),
                ('ult_atual_data', models.DateTimeField(auto_now=True)),
                ('log_n_edicoes', models.IntegerField(default=1)),
                ('ciclo_fase', models.CharField(choices=[('fase_implantacao', 'Implantação'), ('fase_manejo', 'Manejo'), ('fase_experimentacao', 'Experimentação')], max_length=30)),
                ('data', models.DateField()),
                ('status', models.CharField(choices=[('agendado', 'Agendado'), ('executado', 'Executado'), ('cancelado', 'Cancelado')], max_length=20)),
                ('tipo_atividade', models.CharField(choices=[('coleta_amostras', 'Implantação'), ('envio_amostras', 'Manejo'), ('manejo_animal', 'Experimentação'), ('manejo_vegetal', 'Manejo Vegetal'), ('preparacao_solo', 'Preparação do Solo')], max_length=40)),
                ('descricao_atividade', models.TextField(blank=True, default='Não informado.', null=True)),
                ('anexo_titulo', models.CharField(blank=True, max_length=100, null=True)),
                ('anexo_url', models.URLField(blank=True, null=True)),
                ('observacoes_gerais', models.TextField(blank=True, default='Sem observações.', null=True)),
                ('del_status', models.BooleanField(default=False)),
                ('del_data', models.DateTimeField(blank=True, null=True)),
                ('ciclo', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='ciclo_atividade', to='urts.ciclo')),
                ('del_usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='usuario_ciclo_atividade_deletado', to='usuarios.usuarios')),
                ('urt', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='urt_ciclo_atividade', to='urts.urts')),
                ('usuario_atualizacao', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='usuario_ciclo_atividade_edicao', to='usuarios.usuarios')),
                ('usuario_registro', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='usuario_ciclo_atividade_registro', to='usuarios.usuarios')),
            ],
        ),
    ]