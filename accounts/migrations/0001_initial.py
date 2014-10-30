# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('avatar', models.ImageField(upload_to=b'', blank=True)),
                ('website', models.URLField(blank=True)),
                ('phone_number', models.CharField(max_length=200, blank=True)),
                ('zip_code', models.CharField(max_length=200, blank=True)),
                ('pv_api_token', models.CharField(max_length=200, blank=True)),
                ('toggl_api_token', models.CharField(max_length=200, blank=True)),
                ('hipchat_api_token', models.CharField(max_length=200, blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
