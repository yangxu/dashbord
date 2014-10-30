# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0001_squashed_0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='row',
            name='name',
            field=models.CharField(default=1, max_length=100, blank=True),
            preserve_default=False,
        ),
    ]
