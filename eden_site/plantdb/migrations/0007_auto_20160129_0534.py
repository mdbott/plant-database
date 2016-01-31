# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plantdb', '0006_auto_20160129_0532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lightlevel',
            name='description',
            field=models.CharField(max_length=50, blank=True),
        ),
    ]
