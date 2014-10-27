# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='created',
            new_name='created_at',
        ),
        migrations.AddField(
            model_name='review',
            name='sentiment_label',
            field=models.CharField(default=b'neutral', max_length=30),
            preserve_default=True,
        ),
    ]
