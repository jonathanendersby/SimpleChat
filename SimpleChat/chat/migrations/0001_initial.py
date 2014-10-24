# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('party_a_id', models.CharField(max_length=10, db_index=True)),
                ('party_b_id', models.CharField(max_length=10, db_index=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ChatLines',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.CharField(max_length=512)),
                ('party', models.CharField(max_length=1)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('seen_by_other_party', models.BooleanField()),
                ('chat', models.ForeignKey(to='chat.Chat')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
