# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spotlight', '0004_auto_20160326_1048'),
    ]

    operations = [
        migrations.AddField(
            model_name='spotlight',
            name='slug',
            field=models.CharField(default=b'', max_length=100),
            preserve_default=True,
        ),
    ]
