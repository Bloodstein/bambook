# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-18 07:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20171018_1233'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='total_amount',
            new_name='total_price',
        ),
        migrations.RenameField(
            model_name='productinorder',
            old_name='nmb',
            new_name='count',
        ),
    ]
