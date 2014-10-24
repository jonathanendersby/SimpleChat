# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_auto_20141024_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='date_updated',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
