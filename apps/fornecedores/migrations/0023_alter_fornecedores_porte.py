# Generated by Django 4.2.5 on 2023-11-18 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fornecedores', '0022_alter_cnpj_cnae_classe_descricao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fornecedores',
            name='porte',
            field=models.CharField(choices=[('grande_empresa', 'Grande Empresa'), ('medio_porte', 'Médio Porte'), ('me', 'ME'), ('epp', 'EPP'), ('mei', 'MEI'), ('demais', 'Demais')], max_length=20),
        ),
    ]