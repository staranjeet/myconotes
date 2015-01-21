# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewUrl',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(max_length=10)),
                ('gen_date', models.DateTimeField(verbose_name=b'date generated')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('note', models.CharField(max_length=1000)),
                ('note_gen_date', models.DateTimeField(verbose_name=b'note date generated')),
                ('url', models.ForeignKey(to='notes.NewUrl')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
