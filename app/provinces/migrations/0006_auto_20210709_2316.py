# Generated by Django 2.2 on 2021-07-09 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provinces', '0005_auto_20210707_1702'),
    ]

    operations = [
        migrations.AddField(
            model_name='festivo',
            name='ciudad_cercana',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Ciudad relacionada'),
        ),
        migrations.AddField(
            model_name='festivo',
            name='distancia',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Distancia'),
        ),
    ]