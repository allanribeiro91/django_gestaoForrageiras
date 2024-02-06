# Generated by Django 4.2.5 on 2023-10-09 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fornecedores', '0002_cnpj_natureza_juridica'),
    ]

    operations = [
        migrations.CreateModel(
            name='UF_Municipio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_ibge', models.CharField(max_length=10)),
                ('uf_sigla', models.CharField(max_length=2)),
                ('uf', models.CharField(max_length=20)),
                ('municipio', models.CharField(max_length=35)),
                ('municipio_uf', models.CharField(max_length=40)),
                ('lat_long', models.CharField(max_length=25)),
            ],
        ),
    ]
