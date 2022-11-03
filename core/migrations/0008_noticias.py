# Generated by Django 3.2.15 on 2022-10-27 17:15

import core.models
from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_empresasparceiras_imagem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Noticias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('manchete', models.CharField(max_length=100, verbose_name='Notícia')),
                ('descricao', models.TextField(max_length=300, verbose_name='Descrição')),
                ('image', stdimage.models.StdImageField(force_min_size=False, upload_to=core.models.get_file_path, variations={'thumb': {'crop': True, 'width': 300}}, verbose_name='Imagem')),
                ('link', models.CharField(max_length=200, verbose_name='Link')),
            ],
            options={
                'verbose_name': 'Manchete',
                'verbose_name_plural': 'Manchetes',
            },
        ),
    ]
