# Generated by Django 5.1.5 on 2025-03-03 00:01

import usuarios.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_alter_infousuario_foto_perfil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infousuario',
            name='foto_perfil',
            field=models.ImageField(blank=True, null=True, upload_to=usuarios.models.user_directory_path),
        ),
    ]
