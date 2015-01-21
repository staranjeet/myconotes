# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_auto_20150121_1839'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notes',
            old_name='note_gen_date',
            new_name='noteGenDate',
        ),
    ]
