# Generated by Django 2.0 on 2018-12-08 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comum', '0004_auto_20181208_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='arquivo',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Arquivo'),
        ),
        migrations.AlterField(
            model_name='post',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Foto'),
        ),
    ]