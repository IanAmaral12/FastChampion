# Generated by Django 5.1.2 on 2024-11-24 22:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lutadores', '0005_alter_lutadores_contato_alter_lutadores_equipe_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lutadores',
            old_name='experiencia',
            new_name='coach',
        ),
        migrations.RenameField(
            model_name='lutadores',
            old_name='tecnico',
            new_name='nivel',
        ),
    ]