# Generated by Django 5.1.3 on 2024-11-26 04:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lutadores', '0008_alter_lutas_dia_luta'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='lutadores',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lutador_profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
