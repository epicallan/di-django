# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spotlight', '0006_indicator_heading'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indicator',
            name='heading',
            field=models.CharField(default=b'', max_length=200),
            preserve_default=True,
        ),
    ]
