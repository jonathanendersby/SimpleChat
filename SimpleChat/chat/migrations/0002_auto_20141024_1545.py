# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatlines',
            name='seen_by_other_party',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
