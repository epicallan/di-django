# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spotlight', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Indicator',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('short_description', models.CharField(max_length=120)),
                ('description', models.CharField(max_length=150)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
                ('spotlight', models.ForeignKey(to='spotlight.Spotlight')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='indicators',
            name='spotlight',
        ),
        migrations.DeleteModel(
            name='Indicators',
        ),
        migrations.AlterField(
            model_name='spotlight',
            name='description',
            field=models.TextField(),
            preserve_default=True,
        ),
    ]
