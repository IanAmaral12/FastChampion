# Generated by Django 5.1.2 on 2024-11-24 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lutadores', '0004_delete_livros_lutadores_contato_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lutadores',
            name='contato',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='lutadores',
            name='equipe',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='lutadores',
            name='experiencia',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='lutadores',
            name='nome',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='lutadores',
            name='peso',
            field=models.FloatField(max_length=50),
        ),
        migrations.AlterField(
            model_name='lutadores',
            name='tecnico',
            field=models.CharField(max_length=50),
        ),
    ]