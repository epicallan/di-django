# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spotlight', '0002_auto_20160326_0801'),
    ]

    operations = [
        migrations.AddField(
            model_name='indicator',
            name='upload',
            field=models.FileField(default=b'', upload_to=b'uploads/%Y/%m/%d', blank=True),
            preserve_default=True,
        ),
    ]
