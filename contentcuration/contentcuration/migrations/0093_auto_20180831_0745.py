# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-31 07:45
from __future__ import unicode_literals

import contentcuration.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contentcuration', '0092_auto_20180731_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file_on_disk',
            field=models.FileField(blank=True, max_length=500, upload_to=contentcuration.models.object_storage_name),
        ),
    ]
