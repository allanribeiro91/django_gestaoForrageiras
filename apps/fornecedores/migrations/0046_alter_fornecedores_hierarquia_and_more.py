# Generated by Django 4.2.5 on 2023-12-06 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fornecedores', '0045_alter_fornecedores_porte_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fornecedores',
            name='hierarquia',
            field=models.CharField(blank=True, choices=[('filial', 'Filial'), ('matriz', 'Matriz')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='fornecedores',
            name='porte',
            field=models.CharField(choices=[('grande_empresa', 'Grande Empresa'), ('medio_porte', 'Médio Porte'), ('me', 'ME'), ('epp', 'EPP'), ('demais', 'Demais'), ('mei', 'MEI')], max_length=20),
        ),
    ]
