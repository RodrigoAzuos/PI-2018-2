# Generated by Django 2.0 on 2018-12-08 14:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('comum', '0002_post_aceito'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='palavras_chave',
            field=models.CharField(default=django.utils.timezone.now, max_length=255, verbose_name='Palavra_chave'),
            preserve_default=False,
        ),
    ]
