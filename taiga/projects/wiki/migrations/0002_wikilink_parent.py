# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wikilink',
            name='parent',
            field=models.ForeignKey(verbose_name='parent', blank=True, to='wiki.WikiLink', null=True),
            preserve_default=True,
        ),
    ]
