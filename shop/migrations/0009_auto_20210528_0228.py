# Generated by Django 3.2.2 on 2021-05-27 23:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_alter_basket_article_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='IpadVersion',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='basket',
            name='article_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 28, 2, 28, 18, 148131)),
        ),
    ]
