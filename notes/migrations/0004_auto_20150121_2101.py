# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_auto_20150121_1856'),
    ]

    operations = [
        migrations.DeleteModel(
            name='NewUrl',
        ),
        migrations.AddField(
            model_name='notes',
            name='noteid',
            field=models.CharField(default='', max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='notes',
            name='title',
            field=models.CharField(default='h', max_length=100),
            preserve_default=False,
        ),
    ]
