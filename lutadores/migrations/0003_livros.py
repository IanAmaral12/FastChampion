# Generated by Django 5.1.2 on 2024-11-24 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lutadores', '0002_remove_lutadores_idade_lutadores_data_nascimento'),
    ]

    operations = [
        migrations.CreateModel(
            name='Livros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('n_paginas', models.IntegerField()),
            ],
        ),
    ]
