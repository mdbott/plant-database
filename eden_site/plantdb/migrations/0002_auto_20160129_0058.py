# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plantdb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EdibleReference',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reference', models.CharField(blank=True, max_length=20, choices=[(b'Page Reference', b'Page Reference'), (b'Website', b'Website'), (b'Journal', b'Tolerates')])),
                ('notes', models.CharField(max_length=100, blank=True)),
            ],
            options={
                'ordering': ['edible'],
            },
        ),
        migrations.RemoveField(
            model_name='edible_reference',
            name='edible',
        ),
        migrations.RemoveField(
            model_name='edible_reference',
            name='referenceLink',
        ),
        migrations.AlterModelOptions(
            name='soilproperty',
            options={'verbose_name_plural': 'Soil Properties'},
        ),
        migrations.RenameField(
            model_name='soilrelation',
            old_name='relationtype',
            new_name='relationType',
        ),
        migrations.RenameField(
            model_name='soilrelation',
            old_name='soilproperty',
            new_name='soilProperty',
        ),
        migrations.RemoveField(
            model_name='cultivar',
            name='lowerhardiness',
        ),
        migrations.RemoveField(
            model_name='plant',
            name='wind',
        ),
        migrations.AddField(
            model_name='cultivar',
            name='wind_tolerance',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='soilrelation',
            name='relationIntensity',
            field=models.CharField(blank=True, max_length=20, choices=[(b'Low', b'Low'), (b'Medium', b'Medium'), (b'Large', b'Large')]),
        ),
        migrations.AlterField(
            model_name='cultivar',
            name='months_seed_ripe',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='cultivar',
            name='name',
            field=models.CharField(default=b'Base Cultivar', max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='edible',
            name='edible_link',
            field=models.ManyToManyField(to='plantdb.ReferenceList', through='plantdb.EdibleReference', blank=True),
        ),
        migrations.DeleteModel(
            name='Edible_Reference',
        ),
        migrations.AddField(
            model_name='ediblereference',
            name='edible',
            field=models.ForeignKey(to='plantdb.Edible'),
        ),
        migrations.AddField(
            model_name='ediblereference',
            name='referenceLink',
            field=models.ForeignKey(to='plantdb.ReferenceList'),
        ),
    ]
