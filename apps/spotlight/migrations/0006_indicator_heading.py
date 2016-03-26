# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spotlight', '0005_spotlight_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='indicator',
            name='heading',
            field=models.TextField(default=b'', max_length=200),
            preserve_default=True,
        ),
    ]
