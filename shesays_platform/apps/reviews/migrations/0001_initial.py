# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField(default=b'')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('company', models.ForeignKey(to='companies.Company')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
