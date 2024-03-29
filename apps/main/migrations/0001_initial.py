# Generated by Django 4.2.5 on 2024-02-07 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAccessLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='acesso_usuario', to='usuarios.usuarios')),
            ],
        ),
        migrations.CreateModel(
            name='CustomLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('modulo', models.CharField(max_length=140)),
                ('model', models.CharField(default='Não informado', max_length=60)),
                ('model_id', models.IntegerField(default=0)),
                ('item_id', models.IntegerField()),
                ('item_descricao', models.CharField(max_length=140)),
                ('acao', models.CharField(choices=[('create', 'Create'), ('update', 'Update'), ('delete', 'Delete')], max_length=40)),
                ('observacoes', models.CharField(default='Sem observações.', max_length=240)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='log_usuario', to='usuarios.usuarios')),
            ],
        ),
    ]
