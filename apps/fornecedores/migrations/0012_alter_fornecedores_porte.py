# Generated by Django 4.2.5 on 2023-10-25 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fornecedores', '0011_alter_fornecedores_hierarquia_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fornecedores',
            name='porte',
            field=models.CharField(choices=[('demais', 'Demais'), ('medio_porte', 'Médio Porte'), ('epp', 'EPP'), ('grande_empresa', 'Grande Empresa'), ('mei', 'MEI'), ('me', 'ME')], max_length=20),
        ),
    ]