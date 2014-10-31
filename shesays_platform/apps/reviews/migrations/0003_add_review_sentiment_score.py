# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20141027_0913'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='sentiment_score',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='review',
            name='company',
            field=models.ForeignKey(related_name=b'reviews', to='companies.Company'),
        ),
    ]
