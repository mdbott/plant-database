# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plantdb', '0003_auto_20160129_0152'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Light',
            new_name='LightLevel',
        ),
        migrations.AlterModelOptions(
            name='lightlevel',
            options={'verbose_name': 'Light Level', 'verbose_name_plural': 'Light Levels'},
        ),
        migrations.AlterModelOptions(
            name='mineral',
            options={'verbose_name': 'Soil Mineral'},
        ),
        migrations.AlterModelOptions(
            name='plantlocation',
            options={'verbose_name': 'Plant Location'},
        ),
    ]
