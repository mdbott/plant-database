# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plantdb', '0002_auto_20160129_0058'),
    ]

    operations = [
        migrations.CreateModel(
            name='Light',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('location', models.CharField(blank=True, max_length=20, choices=[(1, b'Full Sun'), (2, b'Partial Shade'), (3, b'Deep Shade')])),
                ('description', models.TextField(max_length=100, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='LightInteraction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('relationType', models.CharField(blank=True, max_length=20, choices=[(b'Requires', b'Requires'), (b'Provides', b'Provides'), (b'Tolerates', b'Tolerates'), (b'Cannot Tolerate', b'Cannot Tolerate')])),
                ('description', models.TextField(blank=True)),
                ('location', models.ForeignKey(to='plantdb.Light')),
            ],
            options={
                'ordering': ['plant'],
            },
        ),
        migrations.RenameField(
            model_name='plant',
            old_name='locationinteraction',
            new_name='locationInteraction',
        ),
        migrations.RenameField(
            model_name='plant',
            old_name='mineralinteraction',
            new_name='mineralInteraction',
        ),
        migrations.AlterField(
            model_name='plantlocation',
            name='location',
            field=models.CharField(blank=True, max_length=20, choices=[(b'Woodland Garden', b'Woodland Garden'), (b'Canopy', b'Canopy'), (b'Secondary', b'Secondary'), (b'Sunny Edge', b'Sunny Edge'), (b'Dappled Shade', b'Dappled Shade'), (b'Shady Edge', b'Shady Edge'), (b'Deep Shade', b'Deep Shade'), (b'Other Habitats', b'Other Habitats'), (b'Cultivated Beds', b'Cultivated Beds'), (b'Ground Cover', b'Ground Cover'), (b'Lawn', b'Lawn'), (b'Meadow', b'Meadow'), (b'Hedge', b'Hedge'), (b'Hedgerow', b'Hedgerow'), (b'Pond', b'Pond'), (b'Bog Garden', b'Bog Garden'), (b'Walls', b'Walls')]),
        ),
        migrations.AlterField(
            model_name='rootstock',
            name='name',
            field=models.CharField(default=b'Base Rootstock', max_length=100),
        ),
        migrations.AddField(
            model_name='lightinteraction',
            name='plant',
            field=models.ForeignKey(related_name='light_entries', to='plantdb.Plant'),
        ),
        migrations.AddField(
            model_name='plant',
            name='lightInteraction',
            field=models.ManyToManyField(to='plantdb.Light', through='plantdb.LightInteraction', blank=True),
        ),
    ]
