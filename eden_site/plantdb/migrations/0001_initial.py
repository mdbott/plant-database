# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('parent_type', models.CharField(max_length=30, blank=True)),
                ('author', models.CharField(default=b'Anonymous', max_length=30, null=True, blank=True)),
                ('title', models.CharField(default=b'Untitled', max_length=80, null=True, blank=True)),
                ('comment', models.CharField(max_length=30, blank=True)),
                ('modified', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Cultivar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'No Cultivars', max_length=100, blank=True)),
                ('notes_on_cultivar', models.TextField(null=True, blank=True)),
                ('synonyms', models.TextField(null=True, blank=True)),
                ('edibility_rating', models.IntegerField(null=True, blank=True)),
                ('medicinal_rating', models.IntegerField(null=True, blank=True)),
                ('upperhardiness', models.IntegerField(default=0, null=True, blank=True)),
                ('lowerhardiness', models.IntegerField(default=0, null=True, blank=True)),
                ('range', models.CharField(max_length=100, null=True, blank=True)),
                ('frost_tender', models.NullBooleanField(default=True)),
                ('leaf_startmonth', models.IntegerField(null=True, blank=True)),
                ('months_in_leaf', models.IntegerField(null=True, blank=True)),
                ('flower_startmonth', models.IntegerField(null=True, blank=True)),
                ('months_in_flower', models.IntegerField(null=True, blank=True)),
                ('production_startmonth', models.IntegerField(null=True, blank=True)),
                ('months_in_production', models.IntegerField(null=True, blank=True)),
                ('seed_start_month', models.IntegerField(null=True, blank=True)),
                ('months_seed_ripe', models.IntegerField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Edible',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ediblity_rating', models.CharField(blank=True, max_length=20, choices=[(b'Poor', b'Poor'), (b'Fair', b'Fair'), (b'Good', b'Good'), (b'Excellent', b'Excellent')])),
                ('notes', models.TextField(max_length=100, blank=True)),
            ],
            options={
                'ordering': ['plant'],
            },
        ),
        migrations.CreateModel(
            name='Edible_Reference',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reference', models.CharField(blank=True, max_length=20, choices=[(b'Page Reference', b'Page Reference'), (b'Website', b'Website'), (b'Journal', b'Tolerates')])),
                ('notes', models.CharField(max_length=100, blank=True)),
                ('edible', models.ForeignKey(to='plantdb.Edible')),
            ],
            options={
                'ordering': ['edible'],
            },
        ),
        migrations.CreateModel(
            name='EdibleType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='LocationInteraction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('relationType', models.CharField(blank=True, max_length=20, choices=[(b'Requires', b'Requires'), (b'Provides', b'Provides'), (b'Tolerates', b'Tolerates'), (b'Cannot Tolerate', b'Cannot Tolerate')])),
                ('relationIntensity', models.CharField(blank=True, max_length=20, choices=[(b'Low', b'Low'), (b'Medium', b'Medium'), (b'Large', b'Large')])),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['plant'],
            },
        ),
        migrations.CreateModel(
            name='Mineral',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, choices=[(b'B', b'Boron'), (b'Ca', b'Calcium'), (b'Cl', b'Chlorine'), (b'Co', b'Cobalt'), (b'Cu', b'Copper'), (b'Fe', b'Iron'), (b'K', b'Potassium'), (b'Mg', b'Magnesium'), (b'N', b'Nitrogen'), (b'Mn', b'Manganese'), (b'Mo', b'Molybdenum'), (b'Na', b'Sodium'), (b'Ni', b'Nickel'), (b'P', b'Phosphorus'), (b'S', b'Sulfur'), (b'Se', b'Selenium'), (b'Si', b'Silicon'), (b'Zn', b'Zinc')])),
                ('description', models.TextField(max_length=100, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='MineralInteraction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('relationType', models.CharField(blank=True, max_length=20, choices=[(b'Requires', b'Requires'), (b'Provides', b'Provides'), (b'Tolerates', b'Tolerates'), (b'Cannot Tolerate', b'Cannot Tolerate')])),
                ('relationIntensity', models.CharField(blank=True, max_length=20, choices=[(b'Low', b'Low'), (b'Medium', b'Medium'), (b'Large', b'Large')])),
                ('description', models.TextField(max_length=100, blank=True)),
                ('mineral', models.ForeignKey(related_name='mineral_entries', to='plantdb.Mineral')),
            ],
            options={
                'ordering': ['plant'],
            },
        ),
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('legacy_pfaf_latin_name', models.CharField(max_length=200, null=True, blank=True)),
                ('family', models.CharField(max_length=100, null=True, blank=True)),
                ('genus', models.CharField(max_length=100, null=True, blank=True)),
                ('hybrid', models.CharField(default=b'', max_length=100, null=True, blank=True)),
                ('species', models.CharField(max_length=100, null=True, blank=True)),
                ('ssp', models.CharField(max_length=100, null=True, blank=True)),
                ('common_name', models.CharField(max_length=100, null=True, blank=True)),
                ('habitat', models.CharField(max_length=1024, null=True, blank=True)),
                ('deciduous_evergreen', models.CharField(default=b'D', max_length=1024, null=True, blank=True)),
                ('nitrogen_fixer', models.BooleanField(default=False)),
                ('supports_wildlife', models.BooleanField(default=False)),
                ('flower_type', models.CharField(default=b'N', max_length=2048, null=True, blank=True)),
                ('pollinators', models.CharField(default=b'N', max_length=1024, null=True, blank=True)),
                ('self_fertile', models.BooleanField(default=False)),
                ('scented', models.CharField(default=b'N', max_length=1024, null=True, blank=True)),
                ('wind', models.BooleanField(default=False)),
                ('pollution', models.BooleanField(default=False)),
                ('cultivation_details', models.TextField(max_length=10024, null=True, blank=True)),
                ('known_hazards', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PlantLocation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('location', models.IntegerField(blank=True, choices=[(1, b'Woodland Garden'), (2, b'Canopy'), (3, b'Secondary'), (4, b'Sunny Edge'), (5, b'Dappled Shade'), (6, b'Shady Edge'), (7, b'Deep Shade'), (8, b'Other Habitats'), (9, b'Cultivated Beds'), (10, b'Ground Cover'), (11, b'Lawn'), (12, b'Meadow'), (13, b'Hedge'), (14, b'Hedgerow'), (15, b'Pond'), (16, b'Bog Garden'), (17, b'Walls')])),
                ('description', models.TextField(max_length=100, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Propagation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=20, choices=[(b'Seed', b'Seed'), (b'Cutting', b'Cutting')])),
                ('description', models.TextField(max_length=100, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PropagationDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('startMonth', models.IntegerField(blank=True)),
                ('numberOfMonths', models.IntegerField(blank=True)),
                ('description', models.TextField(blank=True)),
                ('plant', models.ForeignKey(to='plantdb.Plant')),
                ('propagationMode', models.ForeignKey(to='plantdb.Propagation')),
            ],
            options={
                'ordering': ['plant'],
            },
        ),
        migrations.CreateModel(
            name='ReferenceList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=30, null=True, blank=True)),
                ('author', models.CharField(max_length=100, null=True, blank=True)),
                ('comments', models.CharField(max_length=30, null=True, blank=True)),
                ('publisher', models.CharField(max_length=100, null=True, blank=True)),
                ('publication_date', models.DateTimeField(null=True, blank=True)),
                ('isbn', models.CharField(max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rootstock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'Own Rootstock', max_length=100)),
                ('notes_on_rootstock', models.TextField(null=True, blank=True)),
                ('height', models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True)),
                ('width', models.DecimalField(null=True, max_digits=4, decimal_places=2, blank=True)),
                ('growth_rate', models.CharField(default=b'M', max_length=1, null=True, blank=True)),
                ('plant', models.ForeignKey(to='plantdb.Plant')),
            ],
        ),
        migrations.CreateModel(
            name='SoilProperty',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, blank=True)),
                ('type', models.CharField(max_length=20, choices=[(b'pH', b'pH'), (b'moisture', b'moisture'), (b'Fertility', b'Fertility'), (b'Texture', b'Texture')])),
                ('description', models.CharField(max_length=100, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='SoilRelation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('relationtype', models.CharField(blank=True, max_length=20, choices=[(b'Requires', b'Requires'), (b'Provides', b'Provides'), (b'Tolerates', b'Tolerates'), (b'Cannot Tolerate', b'Cannot Tolerate')])),
                ('description', models.TextField(max_length=100, blank=True)),
                ('rootstock', models.ForeignKey(to='plantdb.Rootstock')),
                ('soilproperty', models.ForeignKey(to='plantdb.SoilProperty')),
            ],
            options={
                'ordering': ['rootstock'],
            },
        ),
        migrations.AddField(
            model_name='rootstock',
            name='soilinteractions',
            field=models.ManyToManyField(to='plantdb.SoilProperty', through='plantdb.SoilRelation', blank=True),
        ),
        migrations.AddField(
            model_name='plant',
            name='locationinteraction',
            field=models.ManyToManyField(to='plantdb.PlantLocation', through='plantdb.LocationInteraction', blank=True),
        ),
        migrations.AddField(
            model_name='plant',
            name='mineralinteraction',
            field=models.ManyToManyField(to='plantdb.Mineral', through='plantdb.MineralInteraction', blank=True),
        ),
        migrations.AddField(
            model_name='plant',
            name='propagation_details',
            field=models.ManyToManyField(to='plantdb.Propagation', through='plantdb.PropagationDetails', blank=True),
        ),
        migrations.AddField(
            model_name='mineralinteraction',
            name='plant',
            field=models.ForeignKey(related_name='plant_entries', to='plantdb.Plant'),
        ),
        migrations.AddField(
            model_name='locationinteraction',
            name='location',
            field=models.ForeignKey(to='plantdb.PlantLocation'),
        ),
        migrations.AddField(
            model_name='locationinteraction',
            name='plant',
            field=models.ForeignKey(related_name='location_entries', to='plantdb.Plant'),
        ),
        migrations.AddField(
            model_name='edible_reference',
            name='referenceLink',
            field=models.ForeignKey(to='plantdb.ReferenceList'),
        ),
        migrations.AddField(
            model_name='edible',
            name='edible_link',
            field=models.ManyToManyField(to='plantdb.ReferenceList', through='plantdb.Edible_Reference', blank=True),
        ),
        migrations.AddField(
            model_name='edible',
            name='edible_part',
            field=models.ForeignKey(to='plantdb.EdibleType'),
        ),
        migrations.AddField(
            model_name='edible',
            name='plant',
            field=models.ForeignKey(related_name='plant_entries', to='plantdb.Cultivar'),
        ),
        migrations.AddField(
            model_name='cultivar',
            name='edible',
            field=models.ManyToManyField(to='plantdb.EdibleType', through='plantdb.Edible', blank=True),
        ),
        migrations.AddField(
            model_name='cultivar',
            name='plant',
            field=models.ForeignKey(to='plantdb.Plant'),
        ),
        migrations.AddField(
            model_name='comments',
            name='parent_id',
            field=models.ForeignKey(to='plantdb.Plant'),
        ),
        migrations.AlterUniqueTogether(
            name='rootstock',
            unique_together=set([('name', 'plant')]),
        ),
        migrations.AlterUniqueTogether(
            name='cultivar',
            unique_together=set([('name', 'plant')]),
        ),
    ]
