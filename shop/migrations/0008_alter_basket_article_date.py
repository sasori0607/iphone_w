# Generated by Django 3.2.2 on 2021-05-27 23:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20210528_0152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='article_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 28, 2, 25, 50, 969713)),
        ),
    ]
