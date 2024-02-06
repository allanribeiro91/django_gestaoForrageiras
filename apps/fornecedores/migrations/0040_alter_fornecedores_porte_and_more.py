# Generated by Django 4.2.5 on 2023-12-03 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fornecedores', '0039_alter_fornecedores_hierarquia_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fornecedores',
            name='porte',
            field=models.CharField(choices=[('mei', 'MEI'), ('demais', 'Demais'), ('medio_porte', 'Médio Porte'), ('grande_empresa', 'Grande Empresa'), ('epp', 'EPP'), ('me', 'ME')], max_length=20),
        ),
        migrations.AlterField(
            model_name='fornecedores',
            name='tipo_direito',
            field=models.CharField(choices=[('privado', 'Privado'), ('público', 'Público')], default='privado', max_length=10),
        ),
    ]
