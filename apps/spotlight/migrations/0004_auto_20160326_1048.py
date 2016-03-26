# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spotlight', '0003_indicator_upload'),
    ]

    operations = [
        migrations.RenameField(
            model_name='indicator',
            old_name='short_description',
            new_name='slug',
        ),
        migrations.AlterField(
            model_name='indicator',
            name='description',
            field=models.TextField(),
            preserve_default=True,
        ),
    ]
