# Generated by Django 4.2.5 on 2023-11-27 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fornecedores', '0026_alter_fornecedores_hierarquia_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fornecedores',
            name='porte',
            field=models.CharField(choices=[('epp', 'EPP'), ('me', 'ME'), ('medio_porte', 'Médio Porte'), ('grande_empresa', 'Grande Empresa'), ('mei', 'MEI'), ('demais', 'Demais')], max_length=20),
        ),
    ]