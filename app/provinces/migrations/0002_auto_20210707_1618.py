# Generated by Django 2.2 on 2021-07-07 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provinces', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comunidad',
            name='latitude',
            field=models.CharField(blank=True, max_length=255, verbose_name='Latitude'),
        ),
        migrations.AddField(
            model_name='comunidad',
            name='longitude',
            field=models.CharField(blank=True, max_length=255, verbose_name='Longitude'),
        ),
        migrations.AddField(
            model_name='comunidad',
            name='pagina_oficial',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Pagina oficial del sitio'),
        ),
    ]
