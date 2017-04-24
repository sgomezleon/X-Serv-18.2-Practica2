# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acorta', '0002_auto_20170424_2013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='urls',
            name='url_short',
        ),
    ]
