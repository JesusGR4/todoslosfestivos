# Generated by Django 2.2 on 2021-07-09 22:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('provinces', '0006_auto_20210709_2316'),
    ]

    operations = [
        migrations.AddField(
            model_name='festivo',
            name='municipio',
            field=models.ForeignKey(default=None, help_text='Municipio a la que pertenece', on_delete=django.db.models.deletion.PROTECT, to='provinces.Municipio', verbose_name='Municipio a la que pertenece'),
            preserve_default=False,
        ),
    ]