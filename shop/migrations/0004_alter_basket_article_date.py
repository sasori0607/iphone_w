# Generated by Django 3.2.2 on 2021-05-19 15:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20210519_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='article_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 19, 18, 14, 49, 445798)),
        ),
    ]
