# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_auto_20141024_1601'),
    ]

    operations = [
        migrations.CreateModel(
            name='Line',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.CharField(max_length=512)),
                ('party', models.CharField(max_length=1)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('seen_by_other_party', models.BooleanField(default=False)),
                ('chat', models.ForeignKey(to='chat.Chat')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='chatlines',
            name='chat',
        ),
        migrations.DeleteModel(
            name='ChatLines',
        ),
    ]
