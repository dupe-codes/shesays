# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings

def update_site_name(apps, schema_editor):
    """ Updates the site name in the database """
    Site = apps.get_model('sites', 'Site')
    db_alias = schema_editor.connection.alias
    site = Site.objects.using(db_alias).get(id=settings.SITE_ID)
    site.domain = settings.DOMAIN_NAME
    site.name = settings.SITE_NAME
    site.save()

class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            update_site_name,
        ),
    ]
