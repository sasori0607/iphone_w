# Generated by Django 3.1.7 on 2021-06-15 15:09

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_auto_20210615_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessoriespart',
            name='MemoryVolume',
            field=models.CharField(blank=True, default='-', max_length=120, null=True, verbose_name='Объем памяти(При наличие)'),
        ),
        migrations.AlterField(
            model_name='accessoriespart',
            name='color',
            field=models.ForeignKey(default='-', on_delete=django.db.models.deletion.CASCADE, to='shop.color', verbose_name='Цвет'),
        ),
        migrations.AlterField(
            model_name='accessoriespart',
            name='modelCase',
            field=models.CharField(blank=True, default='-', max_length=120, null=True, verbose_name='Модель привязки чехла'),
        ),
        migrations.AlterField(
            model_name='basket',
            name='article_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 15, 18, 9, 42, 985486)),
        ),
    ]