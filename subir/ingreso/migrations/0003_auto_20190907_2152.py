# Generated by Django 2.2.4 on 2019-09-08 03:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingreso', '0002_auto_20190907_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingreso',
            name='fecha',
            field=models.DateField(default=datetime.datetime.now, verbose_name='Fecha emision'),
        ),
    ]
