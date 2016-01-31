# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plantdb', '0004_auto_20160129_0323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lightlevel',
            name='location',
            field=models.IntegerField(blank=True, null=True, choices=[(1, b'Full Sun'), (2, b'Partial Shade'), (3, b'Deep Shade')]),
        ),
    ]
