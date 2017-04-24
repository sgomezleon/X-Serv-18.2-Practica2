# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acorta', '0003_remove_urls_url_short'),
    ]

    operations = [
        migrations.AddField(
            model_name='urls',
            name='url_short',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
