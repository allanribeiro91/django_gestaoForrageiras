# Generated by Django 4.2.5 on 2023-12-03 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fornecedores', '0035_alter_fornecedores_porte'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fornecedores',
            name='porte',
            field=models.CharField(choices=[('medio_porte', 'Médio Porte'), ('mei', 'MEI'), ('me', 'ME'), ('grande_empresa', 'Grande Empresa'), ('demais', 'Demais'), ('epp', 'EPP')], max_length=20),
        ),
        migrations.AlterField(
            model_name='fornecedores',
            name='tipo_direito',
            field=models.CharField(choices=[('privado', 'Privado'), ('público', 'Público')], default='privado', max_length=10),
        ),
    ]
