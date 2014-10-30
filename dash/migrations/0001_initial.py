# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Row',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fileid', models.CharField(max_length=6, db_index=True)),
                ('filetype', models.CharField(db_index=True, max_length=6, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
