# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plantdb', '0005_auto_20160129_0326'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lightlevel',
            name='location',
        ),
        migrations.AddField(
            model_name='lightlevel',
            name='intensity',
            field=models.IntegerField(blank=True, null=True, choices=[(3, b'Full Sun'), (2, b'Partial Shade'), (1, b'Deep Shade')]),
        ),
        migrations.AlterField(
            model_name='lightlevel',
            name='description',
            field=models.CharField(max_length=10, blank=True),
        ),
    ]
