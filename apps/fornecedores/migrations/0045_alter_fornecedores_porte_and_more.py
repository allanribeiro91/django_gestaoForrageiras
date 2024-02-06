# Generated by Django 4.2.5 on 2023-12-05 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fornecedores', '0044_alter_fornecedores_hierarquia_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fornecedores',
            name='porte',
            field=models.CharField(choices=[('epp', 'EPP'), ('me', 'ME'), ('demais', 'Demais'), ('grande_empresa', 'Grande Empresa'), ('mei', 'MEI'), ('medio_porte', 'Médio Porte')], max_length=20),
        ),
        migrations.AlterField(
            model_name='fornecedores',
            name='tipo_direito',
            field=models.CharField(choices=[('privado', 'Privado'), ('público', 'Público')], default='privado', max_length=10),
        ),
    ]