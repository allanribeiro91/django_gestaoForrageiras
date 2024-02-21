# Generated by Django 4.2.5 on 2024-02-07 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
        ('urts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ciclo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registro_data', models.DateTimeField(auto_now_add=True)),
                ('ult_atual_data', models.DateTimeField(auto_now=True)),
                ('log_n_edicoes', models.IntegerField(default=1)),
                ('numero_ciclo', models.IntegerField()),
                ('fase1', models.CharField(blank=True, max_length=15, null=True)),
                ('fase2', models.CharField(blank=True, max_length=15, null=True)),
                ('fase3', models.CharField(blank=True, max_length=15, null=True)),
                ('observacoes_gerais', models.TextField(blank=True, default='Sem observações.', null=True)),
                ('del_status', models.BooleanField(default=False)),
                ('del_data', models.DateTimeField(blank=True, null=True)),
                ('del_usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='usuario_ciclo_deletado', to='usuarios.usuarios')),
                ('urt', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='urt_ciclo', to='urts.urts')),
                ('usuario_atualizacao', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='usuario_ciclo_edicao', to='usuarios.usuarios')),
                ('usuario_registro', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='usuario_ciclo_registro', to='usuarios.usuarios')),
            ],
        ),
        migrations.CreateModel(
            name='CicloPeriodosClimaticos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registro_data', models.DateTimeField(auto_now_add=True)),
                ('ult_atual_data', models.DateTimeField(auto_now=True)),
                ('log_n_edicoes', models.IntegerField(default=1)),
                ('periodo_climatico', models.CharField(choices=[('chuvoso', 'Chuvoso'), ('seco', 'Seco')], max_length=10)),
                ('data_inicio', models.DateField(blank=True, null=True)),
                ('data_fim', models.DateField(blank=True, null=True)),
                ('observacoes_gerais', models.TextField(blank=True, default='Sem observações.', null=True)),
                ('del_status', models.BooleanField(default=False)),
                ('del_data', models.DateTimeField(blank=True, null=True)),
                ('ciclo', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='ciclo_periodo', to='urts.ciclo')),
                ('del_usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='usuario_ciclo_periodo_deletado', to='usuarios.usuarios')),
                ('urt', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='urt_ciclo_periodo', to='urts.urts')),
                ('usuario_atualizacao', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='usuario_ciclo_periodo_edicao', to='usuarios.usuarios')),
                ('usuario_registro', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='usuario_ciclo_periodo_registro', to='usuarios.usuarios')),
            ],
        ),
        migrations.CreateModel(
            name='CicloEspeciesVegetais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registro_data', models.DateTimeField(auto_now_add=True)),
                ('ult_atual_data', models.DateTimeField(auto_now=True)),
                ('log_n_edicoes', models.IntegerField(default=1)),
                ('especie_vegetal', models.CharField(max_length=140)),
                ('variedades', models.CharField(blank=True, max_length=140, null=True)),
                ('observacoes_gerais', models.TextField(blank=True, default='Sem observações.', null=True)),
                ('del_status', models.BooleanField(default=False)),
                ('del_data', models.DateTimeField(blank=True, null=True)),
                ('ciclo', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='ciclo_vegetal', to='urts.ciclo')),
                ('del_usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='usuario_ciclo_vegetal_deletado', to='usuarios.usuarios')),
                ('urt', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='urt_ciclo_vegetal', to='urts.urts')),
                ('usuario_atualizacao', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='usuario_ciclo_vegetal_edicao', to='usuarios.usuarios')),
                ('usuario_registro', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='usuario_ciclo_vegetal_registro', to='usuarios.usuarios')),
            ],
        ),
        migrations.CreateModel(
            name='CicloEspeciesAnimais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registro_data', models.DateTimeField(auto_now_add=True)),
                ('ult_atual_data', models.DateTimeField(auto_now=True)),
                ('log_n_edicoes', models.IntegerField(default=1)),
                ('especie_animal', models.CharField(max_length=140)),
                ('racas', models.CharField(blank=True, max_length=140, null=True)),
                ('observacoes_gerais', models.TextField(blank=True, default='Sem observações.', null=True)),
                ('del_status', models.BooleanField(default=False)),
                ('del_data', models.DateTimeField(blank=True, null=True)),
                ('ciclo', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='ciclo_animal', to='urts.ciclo')),
                ('del_usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='usuario_ciclo_animal_deletado', to='usuarios.usuarios')),
                ('urt', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='urt_ciclo_animal', to='urts.urts')),
                ('usuario_atualizacao', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='usuario_ciclo_animal_edicao', to='usuarios.usuarios')),
                ('usuario_registro', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='usuario_ciclo_animal_registro', to='usuarios.usuarios')),
            ],
        ),
        migrations.CreateModel(
            name='CicloAtividades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registro_data', models.DateTimeField(auto_now_add=True)),
                ('ult_atual_data', models.DateTimeField(auto_now=True)),
                ('log_n_edicoes', models.IntegerField(default=1)),
                ('fase', models.CharField(choices=[('fase_implantacao', 'Implantação'), ('fase_manejo', 'Manejo'), ('fase_experimentacao', 'Experimentação')], max_length=30)),
                ('data', models.DateField()),
                ('status', models.CharField(choices=[('agendado', 'Agendado'), ('executado', 'Executado'), ('cancelado', 'Cancelado')], max_length=20)),
                ('tipo_atividade', models.CharField(choices=[('coleta_amostras', 'Implantação'), ('envio_amostras', 'Manejo'), ('manejo_animal', 'Experimentação'), ('manejo_vegetal', 'Manejo Vegetal'), ('preparacao_solo', 'Preparação do Solo')], max_length=40)),
                ('descricao_atividade', models.TextField(blank=True, default='Não informado.', null=True)),
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