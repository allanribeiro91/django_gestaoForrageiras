# Generated by Django 4.2.5 on 2023-12-04 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0010_rename_alocacao_alocacoes_rename_usuario_usuarios'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alocacoes',
            name='unidade',
            field=models.CharField(choices=[('', 'Não Informado'), ('dateg', 'DATeG'), ('icna', 'ICNA')], max_length=20),
        ),
    ]