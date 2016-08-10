# from django.db import models
# -*- coding: utf-8 -*-
from django.contrib.gis.db import models
from colorfield.fields import ColorField
from .fields import RGBColorField
#from functools import partial
# from threading import local
#
# _thread_locals = local()
#
#
# def get_rootstock_list():
#     return getattr(getattr(_thread_locals, 'user', None), 'id', None)
#
#
# class ThreadLocals(object):
#     """Middleware that gets various objects from the
#     request object and saves them in thread local storage."""
#     def process_request(self, request):
#         _thread_locals.user = getattr(request, 'user', None)

# Create your models here.
# Mineral Class Definitions
#
# This arrangement allows the enumeration of the minerals that
# each plant requires or provides


class MinMaxFloat(models.FloatField):
    def __init__(self, min_value=None, max_value=None, *args, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        super(MinMaxFloat, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value': self.max_value}
        defaults.update(kwargs)
        return super(MinMaxFloat, self).formfield(**defaults)


class Mineral(models.Model):
    MINERAL_CHOICES = (('B',  'Boron'),
                       ('Ca', 'Calcium'),
                       ('Cl', 'Chlorine'),
                       ('Co', 'Cobalt'),
                       ('Cu', 'Copper'),
                       ('Fe', 'Iron'),
                       ('K', 'Potassium'),
                       ('Mg', 'Magnesium'),
                       ('N',  'Nitrogen'),
                       ('Mn', 'Manganese'),
                       ('Mo', 'Molybdenum'),
                       ('Na', 'Sodium'),
                       ('Ni', 'Nickel'),
                       ('P', 'Phosphorus'),
                       ('S', 'Sulfur'),
                       ('Se', 'Selenium'),
                       ('Si', 'Silicon'),
                       ('Zn', 'Zinc'))
    name = models.CharField(max_length=20, choices=MINERAL_CHOICES)
    description = models.TextField(max_length=100, blank=True)

    def __unicode__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Soil Mineral'


# class LightLevel(models.Model):
#     FULLSUN = 3
#     PARTIALSHADE = 2
#     DEEPSHADE = 1
#     CATEGORIES = (
#             (FULLSUN, 'Full Sun'),
#             (PARTIALSHADE, 'Partial Shade'),
#             (DEEPSHADE, 'Deep Shade'),
#         )
#     lightLevels = dict(CATEGORIES)
#     intensity = models.IntegerField(choices=CATEGORIES, blank=True, null=True)
#     description = models.CharField(max_length=50, blank=True)
#
#     def __unicode__(self):
#         return "%s" % self.description
#
#     class Meta:
#         verbose_name = 'Light Level'
#         verbose_name_plural = 'Light Levels'
# Plant Location Class Definitions
#
# This arrangement allows the enumeration of the plant  that
# each plant requires, tolerates or provides


class PlantLocation(models.Model):

    CATEGORIES = (
            ('Woodland Garden', 'Woodland Garden'),
            ('Canopy', 'Canopy'),
            ('Secondary', 'Secondary'),
            ('Sunny Edge', 'Sunny Edge'),
            ('Dappled Shade', 'Dappled Shade'),
            ('Shady Edge', 'Shady Edge'),
            ('Deep Shade', 'Deep Shade'),
            ('Other Habitats', 'Other Habitats'),
            ('Cultivated Beds', 'Cultivated Beds'),
            ('Ground Cover', 'Ground Cover'),
            ('Lawn', 'Lawn'),
            ('Meadow', 'Meadow'),
            ('Hedge', 'Hedge'),
            ('Hedgerow', 'Hedgerow'),
            ('Pond', 'Pond'),
            ('Bog Garden', 'Bog Garden'),
            ('Walls', 'Walls'),
        )

    location = models.CharField(max_length=20, choices=CATEGORIES, blank=True)
    description = models.TextField(max_length=100, blank=True)

    def __unicode__(self):
        return "%s" % self.location

    class Meta:
        verbose_name = 'Plant Location'
# Propagation Class Definitions
#
# The details are kept in the PropagationDetails model


class Propagation(models.Model):

    PROPAGATION_CHOICES = (('Seed', 'Seed'),
                           ('Cutting', 'Cutting'))

    type = models.CharField(max_length=20, choices=PROPAGATION_CHOICES)
    description = models.TextField(max_length=100, blank=True)


class PlantUse(models.Model):

    use = models.CharField(max_length=20)
    description = models.TextField(max_length=100, blank=True, null=True)

    def __unicode__(self):
        return "%s" % self.use


class References(models.Model):

    RefRating = (
            (1, '1'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5')
        )

    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50, blank=True, null=True)
    internet_address = models.CharField(max_length=30, blank=True, null=True)
    rating = models.IntegerField(blank=True, choices=RefRating, null=True)
    publisher = models.CharField(max_length=100, blank=True, null=True)
    publication_year = models.IntegerField(blank=True, null=True)
    isbn = models.CharField(max_length=30, blank=True, null=True)
    comments = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.title


class ColourTest(models.Model):
    border_colour = RGBColorField(default='#00FF00')


class Plant(models.Model):
    Unknown = -1
    Calm = 0                # 1 km/hr
    LightAir = 1            # 2-5 km/hr
    LightBreeze = 2         # 6-11 km/hr
    GentleBreeze = 3        # 12-19 km/hr
    ModerateBreeze = 4      # 20-28 km/hr
    FreshBreeze = 5         # 29-38 km/hr
    StrongBreeze = 6        # 39-49 km/hr
    NearGale = 7            # 50-61 km/hr
    Gale = 8                # 62-74 km/hr
    SevereGale = 9          # 75-88 km/hr
    Storm = 10              # 89-102 km/hr

    WindLevel = (
        (Unknown, 'Not known'),
        (Calm, 'Calm'),
        (LightAir, 'Light Air'),
        (LightBreeze, 'Light Breeze'),
        (GentleBreeze, 'Gentle Breeze'),
        (ModerateBreeze, 'Moderate Breeze'),
        (FreshBreeze, 'Fresh Breeze'),
        (StrongBreeze, 'Strong Breeze'),
        (NearGale, 'Near Gale'),
        (Gale, 'Gale'),
        (SevereGale, 'Severe Gale'),
        (Storm, 'Storm')
    )

    FullSun = 3
    PartialShade = 2
    DeepShade = 1
    LightLevel = (
            (FullSun, 'Full Sun'),
            (PartialShade, 'Partial Shade'),
            (DeepShade, 'Deep Shade'),
        )

    # Plant Function
    Productive = 1
    Support = 2
    Weed = 3
    Native = 4
    PlantFunction = (
        (Productive, 'Productive Species'),
        (Support, 'Support Species'),
        (Weed, 'Weed/Volunteer Species'),
        (Native, 'Native Species')
    )
    # Plant Form
    LargeTree = 12
    MediumTree = 11
    SmallTree = 10
    Bamboo = 9
    Shrub = 8
    Fern = 7
    ProstrateShrub = 6
    Vine = 5
    Herbaceous = 4
    Bulb = 3
    Biennial = 2
    Annual = 1
    Form = (
        (LargeTree, 'Large Tree'),
        (MediumTree, 'Medium Tree'),
        (SmallTree, 'Small Tree'),
        (Shrub, 'Shrub'),
        (Fern, 'Fern'),
        (ProstrateShrub, 'Prostrate Shrub'),
        (Vine, 'Vine'),
        (Herbaceous, 'Herbaceous Species'),
        (Bulb, 'Corm/Bulb'),
        (Biennial, 'Biennial'),
        (Annual, 'Annual Species')
    )

    PlantShape = (
        ('Spike_1', 'Spiked Form 1'),
        ('Spike_2', 'Spiked Form 2'),
        ('Spike_3', 'Spiked Form 3'),
        ('Spike_4', 'Spiked Form 4'),
        ('Mounded_1', 'Mounded Form 1'),
        ('Mounded_2', 'Mounded Form 2'),
        ('Prostrate_1', 'Prostrate Form 1'),
        ('Prostrate_2', 'Prostrate Form 2'),
        ('Prostrate_3', 'Prostrate Form 3'),
        ('Prostrate_4', 'Prostrate Form 4'),
        ('Fountain_1', 'Fountain Form 1'),
        ('Fountain_2', 'Fountain Form 2'),
        ('Columnar_1', 'Columnar Form 1'),
        ('Oval_1', 'Oval Form 1'),
        ('Pyramidal_1', 'Pyramidal Form 1'),
        ('Rounded_1', 'Rounded Form 1'),
        ('Rounded_2', 'Rounded Form 2'),
        ('Spreading_1', 'Spreading Form 1'),
        ('Spreading_2', 'Spreading Form 2'),
        ('Vase_1', 'Vase Form 1'),
        ('Vase_2', 'Vase Form 2'),
        ('Vase_3', 'Vase Form 3'),
        ('Vase_4', 'Vase Form 4'),
        ('Weeping_1', 'Weeping Form 1')
    )

    # Flower Type
    Hermaphrodite = 1
    Monoecious = 2
    Dioecious = 3
    FlowerType = (
        (Hermaphrodite, 'Hermaphrodite (the flower has both male and female organs)'),
        (Monoecious, 'Monoecious (individual flowers are either male or female, but both sexes can be found on the \
        same plant)'),
        (Dioecious, 'dioecious (individual flowers are either male or female, but only one sex is to be found on \
        any one plant so both male and female plants must be grown if seed is required)')
    )

    legacy_pfaf_latin_name = models.CharField(max_length=200, blank=True, null=True)
    family = models.CharField(max_length=100, blank=True, null=True)
    genus = models.CharField(max_length=100, blank=True, null=True)
    hybrid = models.CharField(max_length=100, blank=True, default='', null=True)
    species = models.CharField(max_length=100, blank=True, null=True)
    ssp = models.CharField(max_length=100, blank=True, null=True)
    common_name = models.CharField(max_length=100, blank=True, null=True)
    plant_function = models.IntegerField(blank=True, choices=PlantFunction, null=True)
    plant_uses = models.ManyToManyField(PlantUse, blank=True, through='Usage')
    form = models.IntegerField(blank=True, choices=Form, null=True)
    habitat = models.CharField(max_length=1024, blank=True, null=True)
    # icon_path = models.CharField(max_length=100, blank=True, null=True)
    border_colour = RGBColorField(default='#00FF00')
    fill_colour = RGBColorField(default='#000000')
    symbol = models.CharField(max_length=50, default='Rounded_1', choices=PlantShape)
    wind_lower_limit = models.IntegerField(blank=True, choices=WindLevel, null=True)
    wind_upper_limit = models.IntegerField(blank=True, choices=WindLevel, null=True)
    light_lower_limit = models.IntegerField(blank=True, choices=LightLevel, null=True)
    light_upper_limit = models.IntegerField(blank=True, choices=LightLevel, null=True)
    deciduous_evergreen = models.CharField(max_length=1024, blank=True, default='D', null=True)
    nitrogen_fixer = models.BooleanField(default=False)
    supports_wildlife = models.BooleanField(default=False)
    flower_type = models.IntegerField(blank=True, choices=FlowerType, null=True)
    pollinators = models.CharField(max_length=1024, blank=True, default='N', null=True)
    self_fertile = models.BooleanField(default=False)
    pollution = models.BooleanField(default=False)
    mineralInteraction = models.ManyToManyField(Mineral, blank=True, through='MineralInteraction')
    locationInteraction = models.ManyToManyField(PlantLocation, blank=True, through='LocationInteraction')
    # lightInteraction = models.ManyToManyField(LightLevel, blank=True, through='LightInteraction')
    cultivation_details = models.TextField(max_length=10024, blank=True, null=True)
    propagation_details = models.ManyToManyField(Propagation, blank=True, through='PropagationDetails')
    known_hazards = models.TextField(blank=True, null=True)
    source_reference = models.ForeignKey(References, on_delete=models.CASCADE, related_name='source_entries')
    references = models.ManyToManyField(References, blank=True, through='ReferenceDetail')

    # class Meta:
    #    unique_together = ('family' , 'genus' , 'species' , 'ssp')

    def __unicode__(self):
        return "%s" % self.legacy_pfaf_latin_name


# class SoilProperty(models.Model):
#     PROPERTY = (
#         ('Soil pH', 'Soil pH'),
#         ('Soil Moisture', 'Soil Moisture'),
#         ('Soil Salinity', 'Soil Salinity'),
#         ('Silt Level', 'Silt Level'),
#         ('Sand Level', 'Sand Level'),
#         ('Clay Level', 'Clay Level'),
#    )
    # TEXTURE = 1
    # pH = 2
    # MOISTURE = 3
    # SALINITY = 4
    # INTPROPERTY = (
    #     (TEXTURE, 'Soil Texture'),
    #     (pH, 'Soil pH'),
    #     (MOISTURE, 'Soil Moisture'),
    #     (SALINITY, 'Soil Salinity'),
    # )

    # use = models.CharField(max_length=20, choices=PROPERTY)
    # # models.IntegerField(blank=True, choices=INTPROPERTY)
    # description = models.CharField(max_length=100, blank=True)
    #
    # def __unicode__(self):
    #     return self.use
    #
    # class Meta:
    #     verbose_name_plural = "Soil Properties"

# Soil Properties
# pH related
# acid
# neutral
# alkaline
# moisture related
# wet
# moist
# dry
# drought
#
class RootPathogen(models.Model):

    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Root Pathogens"


class Rootstock(models.Model):
    Low = 1
    Medium = 2
    High = 3
    SalinityLevel = (
        (Low, 'Low 2-4 dS/m'),
        (Medium, 'Medium 4-8 dS/m'),
        (High, 'High 8+ dS/m'),
    )
    Dry = 1
    Moist = 2
    Wet = 3
    Water = 4
    MoistureLevel = (
        (Dry, 'Dry Soil'),
        (Moist, 'Moist Soil'),
        (Wet, 'Wet Soil'),
        (Water, 'Water')
    )
    Light = 1
    Medium = 2
    Heavy = 3
    SoilTexture = (
        (Light, 'Light (sandy) soil'),
        (Medium, 'Medium (loamy) soil'),
        (Heavy, 'Heavy (clay) soil')
    )
    rootstockname = models.CharField(max_length=100, default='Base Rootstock')
    base_rootstock = models.BooleanField(default=False)
    notes_on_rootstock = models.TextField(blank=True, null=True)
    plant = models.ForeignKey(Plant)
    height = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2)
    width = models.DecimalField(blank=True, null=True, max_digits=4, decimal_places=2)
    vigour = models.CharField(max_length=1, blank=True, default='M', null=True)
    pH_lower_limit = MinMaxFloat(min_value=4.0, max_value=10.0, blank=True, null=True)
    pH_upper_limit = MinMaxFloat(min_value=4.0, max_value=10.0, blank=True, null=True)
    salinity_lower_limit = models.IntegerField(blank=True, choices=SalinityLevel, null=True)
    salinity_upper_limit = models.IntegerField(blank=True, choices=SalinityLevel, null=True)
    moisture_lower_limit = models.IntegerField(blank=True, choices=MoistureLevel, null=True)
    moisture_upper_limit = models.IntegerField(blank=True, choices=MoistureLevel, null=True)
    soiltexture_lower_limit = models.IntegerField(blank=True, choices=SoilTexture, null=True)
    soiltexture_upper_limit = models.IntegerField(blank=True, choices=SoilTexture, null=True)
    soildiseaseinteractions = models.ManyToManyField(RootPathogen, blank=True, through='RootPathogenResistance')

    def __unicode__(self):
        return self.rootstockname

    class Meta:
        unique_together = ('rootstockname', 'plant')


    # def _product_list(self, cls):
    #     """
    #     return a list containing the one product_id contained in the request URL,
    #     or a query containing all valid product_ids if not id present in URL
    #
    #     used to limit the choice of foreign key object to those related to the current product
    #     """
    #     id = threadlocals.get_current_product()
    #     if id is not None:
    #         return [id]
    #     else:
    #         return Product.objects.all().values('pk').query


# class ReferenceList(models.Model):
#     title = models.CharField(max_length=30, blank=True, null=True)
#     author = models.CharField(max_length=100, blank=True, null=True)
#     internet_address = models.CharField(max_length=30, blank=True, null=True)
#     comments = models.CharField(max_length=30, blank=True, null=True)
#     publisher = models.CharField(max_length=100, blank=True, null=True)
#     publication_date = models.DateTimeField(blank=True, null=True)
#     isbn = models.CharField(max_length=100, blank=True, null=True)


# Soil Relation Tables for the each Rootstock

# class SoilRequirement(models.Model):
#
#     CATEGORIES = (
#         ('Lower Limit', 'Lower Limit'),
#         ('Upper Limit', 'Upper Limit')
#     )
#     RATING = (
#             ('Low', 'Low'),
#             ('Medium', 'Medium'),
#             ('High', 'High'))
#
#     rootstock = models.ForeignKey(Rootstock)
#     soilProperty = models.ForeignKey(SoilProperty)
#     LowerLimitValue = models.FloatField(null=True, blank=True, default=None)
#     UpperLimitValue = models.FloatField(null=True, blank=True, default=None)
#     LowerLimitIntensity = models.CharField(max_length=20, choices=RATING, blank=True)
#     UpperLimitIntensity = models.CharField(max_length=20, choices=RATING, blank=True)
#
#
#     class Meta:
#         ordering = ['rootstock']


class RootPathogenResistance(models.Model):

    RATING = (
            ('Susceptible', 'Susceptible'),
            ('Moderately Resistant', 'Moderately Resistant'),
            ('Highly Resistant', 'Highly Resistant'),
            ('Resistant', 'Resistant'),
    )

    rootstock = models.ForeignKey(Rootstock)
    Pathogen = models.ForeignKey(RootPathogen)
    Resistance = models.CharField(max_length=20, choices=RATING, blank=True)

    class Meta:
        ordering = ['rootstock']


class EdibleUse(models.Model):
    use = models.CharField(max_length=20, blank=True)
    description = models.TextField(max_length=100, blank=True, null=True)

    def __unicode__(self):
        return self.use


class MedicinalUse(models.Model):
    use = models.CharField(max_length=20, blank=True)
    description = models.TextField(max_length=100, blank=True, null=True)

    def __unicode__(self):
        return self.use


class Cultivar(models.Model):

    JANUARY = 1
    FEBRUARY = 2
    MARCH = 3
    APRIL = 4
    MAY = 5
    JUNE = 6
    JULY = 7
    AUGUST = 8
    SEPTEMBER = 9
    OCTOBER = 10
    NOVEMBER = 11
    DECEMBER = 12
    MONTH = (
        (JANUARY, 'January'),
        (FEBRUARY, 'Feburary'),
        (MARCH, 'March'),
        (APRIL, 'April'),
        (MAY, 'May'),
        (JUNE, 'June'),
        (JULY, 'July'),
        (AUGUST, 'August'),
        (SEPTEMBER, 'September'),
        (OCTOBER, 'October'),
        (NOVEMBER, 'November'),
        (DECEMBER, 'December')
    )

    Hardiness_Zone = (
        (0, 'Hardiness Zone 0a  less than -53.9 °C (-65 °F)'),
        (1, 'Hardiness Zone 0b  -53.9 °C (-65 °F) to -51.1°C (60 °F)'),
        (2, 'Hardiness Zone 1a 	−51.1 °C (−60 °F) to −48.3 °C (−55 °F)'),
        (3, 'Hardiness Zone 1b 	−48.3 °C (−55 °F) to −45.6 °C (−50 °F)'),
        (4, 'Hardiness Zone 2a 	−45.6 °C (−50 °F) to −42.8 °C (−45 °F)'),
        (5, 'Hardiness Zone 2b 	−42.8 °C (−45 °F) to −40 °C (−40 °F)'),
        (6, 'Hardiness Zone 3a 	−40 °C (−40 °F) to −37.2 °C (−35 °F)'),
        (7, 'Hardiness Zone 3b 	−37.2 °C (−35 °F) to −34.4 °C (−30 °F)'),
        (8, 'Hardiness Zone 4a 	−34.4 °C (−30 °F) to −31.7 °C (−25 °F)'),
        (9, 'Hardiness Zone 4b 	−31.7 °C (−25 °F) to −28.9 °C (−20 °F)'),
        (10, 'Hardiness Zone 5a 	−28.9 °C (−20 °F) to −26.1 °C (−15 °F)'),
        (11, 'Hardiness Zone 5b 	−26.1 °C (−15 °F) to −23.3 °C (−10 °F)'),
        (12, 'Hardiness Zone 6a 	−23.3 °C (−10 °F) to −20.6 °C (−5 °F)'),
        (13, 'Hardiness Zone 6b 	−20.6 °C (−5 °F) to −17.8 °C (0 °F)'),
        (14, 'Hardiness Zone 7a 	−17.8 °C (0 °F) to −15 °C (5 °F)'),
        (15, 'Hardiness Zone 7b 	−15 °C (5 °F) to −12.2 °C (10 °F)'),
        (16, 'Hardiness Zone 8a 	−12.2 °C (10 °F) to −9.4 °C (15 °F)'),
        (17, 'Hardiness Zone 8b 	−9.4 °C (15 °F) to −6.7 °C (20 °F)'),
        (18, 'Hardiness Zone 9a 	−6.7 °C (20 °F) to −3.9 °C (25 °F)'),
        (19, 'Hardiness Zone 9b 	−3.9 °C (25 °F) to −1.1 °C (30 °F)'),
        (20, 'Hardiness Zone 10a 	−1.1 °C (30 °F) to +1.7 °C (35 °F)'),
        (21, 'Hardiness Zone 10b 	+1.7 °C (35 °F) to +4.4 °C (40 °F)'),
        (22, 'Hardiness Zone 11a 	+4.4 °C (40 °F) to +7.2 °C (45 °F)'),
        (23, 'Hardiness Zone 11b 	+7.2 °C (45 °F) to +10 °C (50 °F)'),
        (24, 'Hardiness Zone 12a 	+10 °C (50 °F) to +12.8 °C (55 °F)'),
        (25, 'Hardiness Zone 12b 	greater than+12.8 °C (55 °F)')
    )

    Heat_Zone = (
        (1, 'Heat Zone 1: 0 days over 30°C'),
        (2, 'Heat Zone 2: 1 to 7 days over 30°C'),
        (3, 'Heat Zone 3: 8 to 14 days over 30°C'),
        (4, 'Heat Zone 4: 15 to 30 days over 30°C'),
        (5, 'Heat Zone 5: 31 to 45 days over 30°C'),
        (6, 'Heat Zone 6: 46 to	60 days over 30°C'),
        (7, 'Heat Zone 7: 61 to 90 days over 30°C'),
        (8, 'Heat Zone 8: 91 to 120 days over 30°C'),
        (9, 'Heat Zone 9: 121 to 150 days over 30°C'),
        (10, 'Heat Zone 10: 151 to 180 days over 30°C'),
        (11, 'Heat Zone 11: 181 to 210 days over 30°C'),
        (12, 'Heat Zone 12: more than 210 days over 30°C')
    )

    name = models.CharField(max_length=100, default='Base Cultivar', blank=True)
    base_cultivar = models.BooleanField(default=False)
    notes_on_cultivar = models.TextField(blank=True, null=True)
    synonyms = models.TextField(blank=True, null=True)
    plant = models.ForeignKey(Plant)
    edible = models.ManyToManyField(EdibleUse, blank=True, through='Edible')
    medicinal = models.ManyToManyField(MedicinalUse, blank=True, through='Medicinal')
    scented = models.NullBooleanField(default=False, blank=True, null=True)
    wind_tolerance = models.IntegerField(blank=True, null=True)
    hardiness_lower_limit = models.IntegerField(default=17, choices=Hardiness_Zone, blank=True, null=True)
    hardiness_upper_limit = models.IntegerField(default=17, choices=Hardiness_Zone, blank=True, null=True)
    heatzone_lower_limit = models.IntegerField(default=6, choices=Heat_Zone, blank=True, null=True)
    heatzone_upper_limit = models.IntegerField(default=6, choices=Heat_Zone, blank=True, null=True)
    range = models.CharField(max_length=100, blank=True, null=True)
    frost_tender = models.NullBooleanField(default=True, blank=True, null=True)
    leaf_startmonth = models.IntegerField(blank=True, choices=MONTH, null=True)
    leaf_endmonth = models.IntegerField(blank=True, choices=MONTH, null=True)
    flower_startmonth = models.IntegerField(blank=True, choices=MONTH, null=True)
    flower_endmonth = models.IntegerField(blank=True, choices=MONTH, null=True)
    production_startmonth = models.IntegerField(blank=True, choices=MONTH, null=True)
    production_endmonth = models.IntegerField(blank=True, choices=MONTH, null=True)
    seed_start_month = models.IntegerField(blank=True, choices=MONTH, null=True)
    seed_endmonth = models.IntegerField(blank=True, choices=MONTH, null=True)
    native_rootstock = models.ForeignKey(Rootstock, on_delete=models.CASCADE)
    # Equivalent to 'F' full shade in pfaf shade rating
    # semi_shade              = models.BooleanField(default=True)  # Equivalent to 'S' semi shade in pfaf shade rating
    # no_shade                = models.BooleanField(default=True)  # Equivalent to 'N' no shade in pfaf shade rating

    def __unicode__(self):
        return self.name

    class Meta:
        unique_together = ('name', 'plant')


class Edible(models.Model):

    Edibility = (
            (1, 'Poor'),
            (2, 'Moderate'),
            (3, 'Average'),
            (4, 'Good'),
            (5, 'Excellent'))

    plant = models.ForeignKey(Cultivar, related_name='plant_entries')
    edible_use = models.ForeignKey(EdibleUse)
    edibility_rating = models.IntegerField(blank=True, choices=Edibility, null=True)
    #edible_link = models.ManyToManyField(ReferenceList, blank=True, through='EdibleReference')
    notes = models.TextField(max_length=100, blank=True, null=True)

    class Meta:
        ordering = ['plant']


class Medicinal(models.Model):

    MedicinalValue = (
            (1, 'Poor'),
            (2, 'Moderate'),
            (3, 'Average'),
            (4, 'Good'),
            (5, 'Excellent'))

    plant = models.ForeignKey(Cultivar, related_name='plant_entry')
    medicinal_use = models.ForeignKey(MedicinalUse)
    medicinal_rating = models.IntegerField(blank=True, choices=MedicinalValue, null=True)
    #medicinal_link = models.ManyToManyField(ReferenceList, blank=True, through='MedicinalReference')
    notes = models.TextField(max_length=100, blank=True, null=True)

    class Meta:
        ordering = ['plant']


# Plant Mineral Relationship Class
# class EdibleReference(models.Model):
#
#     CATEGORIES = (
#         ('Page Reference', 'Page Reference'),
#         ('Website', 'Website'),
#         ('Journal', 'Journal'))
#
#     #referenceLink = models.ForeignKey(ReferenceList)
#     edible = models.ForeignKey(Edible)
#     reference = models.CharField(max_length=20, choices=CATEGORIES, blank=True)
#     notes = models.CharField(max_length=100, blank=True)
#
#     class Meta:
#         ordering = ['edible']


# class MedicinalReference(models.Model):
#
#     CATEGORIES = (
#         ('Page Reference', 'Page Reference'),
#         ('Website', 'Website'),
#         ('Journal', 'Journal'))
#
#     referenceLink = models.ForeignKey(ReferenceList)
#     medicinalDetail = models.ForeignKey(Medicinal)
#     reference = models.CharField(max_length=20, choices=CATEGORIES, blank=True)
#     notes = models.CharField(max_length=100, blank=True)
#
#     class Meta:
#         ordering = ['medicinalDetail']


# Plant Mineral Relationship Class
class MineralInteraction(models.Model):

    CATEGORIES = (
        ('Requires', 'Requires'),
        ('Provides', 'Provides'),
        ('Tolerates', 'Tolerates'),
        ('Cannot Tolerate', 'Cannot Tolerate'))
    RATING = (
            ('Low', 'Low'),
            ('Medium', 'Medium'),
            ('Large', 'Large'))

    plant = models.ForeignKey(Plant, related_name='plant_entries')
    mineral = models.ForeignKey(Mineral, related_name='mineral_entries')
    relationType = models.CharField(max_length=20, choices=CATEGORIES, blank=True)
    relationIntensity = models.CharField(max_length=20, choices=RATING, blank=True)
    description = models.TextField(max_length=100, blank=True)

    class Meta:
        ordering = ['plant']


# Plant Location Relationship Class
class LocationInteraction(models.Model):

    CATEGORIES = (
        ('Requires', 'Requires'),
        ('Provides', 'Provides'),
        ('Tolerates', 'Tolerates'),
        ('Cannot Tolerate', 'Cannot Tolerate'))
    RATING = (
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('Large', 'Large'))

    plant = models.ForeignKey(Plant, related_name='location_entries')
    location = models.ForeignKey(PlantLocation)
    relationType = models.CharField(max_length=20, choices=CATEGORIES, blank=True)
    relationIntensity = models.CharField(max_length=20, choices=RATING, blank=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['plant']


# Plant Light Relationship Class
# class LightInteraction(models.Model):
#
#     CATEGORIES = (
#         ('Requires', 'Requires'),
#         ('Provides', 'Provides'),
#         ('Tolerates', 'Tolerates'),
#         ('Cannot Tolerate', 'Cannot Tolerate'))
#
#     plant = models.ForeignKey(Plant, related_name='light_entries')
#     location = models.ForeignKey(LightLevel)
#     relationType = models.CharField(max_length=20, choices=CATEGORIES, blank=True)
#     description = models.TextField(blank=True)
#
#     class Meta:
#         ordering = ['plant']

# Plant Location Relationship Class
class PropagationDetails(models.Model):

    plant = models.ForeignKey(Plant)
    propagationMode = models.ForeignKey(Propagation)
    startMonth = models.IntegerField(blank=True)
    numberOfMonths = models.IntegerField(blank=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['plant']


class ReferenceDetail(models.Model):

    plant = models.ForeignKey(Plant)
    reference = models.ForeignKey(References)
    description = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['plant']


class Usage(models.Model):

    plant = models.ForeignKey(Plant)
    plant_use = models.ForeignKey(PlantUse)
    description = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['plant']


class Comments(models.Model):
    parent_type = models.CharField(max_length=30, blank=True)
    parent_id = models.ForeignKey(Plant)
    author = models.CharField(max_length=30, blank=True, default='Anonymous', null=True)
    title = models.CharField(max_length=80, blank=True, default='Untitled', null=True)
    comment = models.CharField(max_length=30, blank=True, null=False)
    modified = models.DateTimeField()


# GeoDjango Models

class Vegetation(models.Model):
    plant = models.ForeignKey(Plant)
    cultivar = models.ForeignKey(Cultivar)
    rootstock = models.ForeignKey(Rootstock)
    grafted = models.BooleanField(default=False)
    locations = models.PointField(srid=3857)
    comment = models.TextField(blank=True, null=True)
    germination_date = models.DateField(blank=True, null=True)
    objects = models.GeoManager()

    def __unicode__(self):
        return "%s (Cultivar: %s, %s Rootstock)" % (self.plant, self.cultivar, self.rootstock)

    class Meta:
        verbose_name = 'Planting'


class MoistureZone(models.Model):
    Low = 1
    Medium = 2
    High = 3
    MoistureLevel = (
        (Low, 'Low'),
        (Medium, 'Medium'),
        (High, 'High'),
    )
    moisturelevel = models.IntegerField(choices=MoistureLevel)
    locations = models.MultiPolygonField()
    objects = models.GeoManager()


class SalinityZone(models.Model):
    Low = 1
    Medium = 2
    High = 3
    SalinityLevel = (
        (Low, 'Low 2-4 dS/m'),
        (Medium, 'Medium 4-8 dS/m'),
        (High, 'High 8+ dS/m'),
    )
    salinitylevel = models.IntegerField(choices=SalinityLevel)
    locations = models.MultiPolygonField()
    objects = models.GeoManager()


class HardinessZone(models.Model):
    Hardiness_Zone = (
        (0, 'Hardiness Zone 0a  less than -53.9 °C (-65 °F)'),
        (1, 'Hardiness Zone 0b  -53.9 °C (-65 °F) to -51.1°C (60 °F)'),
        (2, 'Hardiness Zone 1a 	−51.1 °C (−60 °F) to −48.3 °C (−55 °F)'),
        (3, 'Hardiness Zone 1b 	−48.3 °C (−55 °F) to −45.6 °C (−50 °F)'),
        (4, 'Hardiness Zone 2a 	−45.6 °C (−50 °F) to −42.8 °C (−45 °F)'),
        (5, 'Hardiness Zone 2b 	−42.8 °C (−45 °F) to −40 °C (−40 °F)'),
        (6, 'Hardiness Zone 3a 	−40 °C (−40 °F) to −37.2 °C (−35 °F)'),
        (7, 'Hardiness Zone 3b 	−37.2 °C (−35 °F) to −34.4 °C (−30 °F)'),
        (8, 'Hardiness Zone 4a 	−34.4 °C (−30 °F) to −31.7 °C (−25 °F)'),
        (9, 'Hardiness Zone 4b 	−31.7 °C (−25 °F) to −28.9 °C (−20 °F)'),
        (10, 'Hardiness Zone 5a −28.9 °C (−20 °F) to −26.1 °C (−15 °F)'),
        (11, 'Hardiness Zone 5b −26.1 °C (−15 °F) to −23.3 °C (−10 °F)'),
        (12, 'Hardiness Zone 6a −23.3 °C (−10 °F) to −20.6 °C (−5 °F)'),
        (13, 'Hardiness Zone 6b −20.6 °C (−5 °F) to −17.8 °C (0 °F)'),
        (14, 'Hardiness Zone 7a −17.8 °C (0 °F) to −15 °C (5 °F)'),
        (15, 'Hardiness Zone 7b −15 °C (5 °F) to −12.2 °C (10 °F)'),
        (16, 'Hardiness Zone 8a −12.2 °C (10 °F) to −9.4 °C (15 °F)'),
        (17, 'Hardiness Zone 8b −9.4 °C (15 °F) to −6.7 °C (20 °F)'),
        (18, 'Hardiness Zone 9a −6.7 °C (20 °F) to −3.9 °C (25 °F)'),
        (19, 'Hardiness Zone 9b −3.9 °C (25 °F) to −1.1 °C (30 °F)'),
        (20, 'Hardiness Zone 10a −1.1 °C (30 °F) to +1.7 °C (35 °F)'),
        (21, 'Hardiness Zone 10b +1.7 °C (35 °F) to +4.4 °C (40 °F)'),
        (22, 'Hardiness Zone 11a +4.4 °C (40 °F) to +7.2 °C (45 °F)'),
        (23, 'Hardiness Zone 11b +7.2 °C (45 °F) to +10 °C (50 °F)'),
        (24, 'Hardiness Zone 12a +10 °C (50 °F) to +12.8 °C (55 °F)'),
        (25, 'Hardiness Zone 12b greater than +12.8 °C (55 °F)')
    )

    Hardinesslevel = models.IntegerField(choices=Hardiness_Zone)
    locations = models.MultiPolygonField()
    objects = models.GeoManager()


class HeatZone(models.Model):

    Heat_Zone = (
        (1, 'Heat Zone 1: less than 1 days over 30°C'),
        (2, 'Heat Zone 2: 2 to 7 days over 30°C'),
        (3, 'Heat Zone 3: 8 to 14 days over 30°C'),
        (4, 'Heat Zone 4: 15 to 30 days over 30°C'),
        (5, 'Heat Zone 5: 31 to 45 days over 30°C'),
        (6, 'Heat Zone 6: 46 to	60 days over 30°C'),
        (7, 'Heat Zone 7: 61 to 90 days over 30°C'),
        (8, 'Heat Zone 8: 91 to 120 days over 30°C'),
        (9, 'Heat Zone 9: 121 to 150 days over 30°C'),
        (10, 'Heat Zone 10: 151 to 180 days over 30°C'),
        (11, 'Heat Zone 11: 181 to 210 days over 30°C'),
        (12, 'Heat Zone 12: more than 210 days over 30°C')
    )

    HeatZonelevel = models.IntegerField(choices=Heat_Zone)
    locations = models.MultiPolygonField()
    objects = models.GeoManager()


class pHZone(models.Model):

    pHlevel = MinMaxFloat(min_value=4.0, max_value=10.0)
    locations = models.MultiPolygonField()
    objects = models.GeoManager()


class WindZone(models.Model):
    Calm = 0                # 1 km/hr
    LightAir = 1            # 2-5 km/hr
    LightBreeze = 2         # 6-11 km/hr
    GentleBreeze = 3        # 12-19 km/hr
    ModerateBreeze = 4      # 20-28 km/hr
    FreshBreeze = 5         # 29-38 km/hr
    StrongBreeze = 6        # 39-49 km/hr
    NearGale = 7            # 50-61 km/hr
    Gale = 8                # 62-74 km/hr
    SevereGale = 9          # 75-88 km/hr
    Storm = 10              # 89-102 km/hr

    WindLevel = (
        (Calm, 'Calm'),
        (LightAir, 'Light Air'),
        (LightBreeze, 'Light Breeze'),
        (GentleBreeze, 'Gentle Breeze'),
        (ModerateBreeze, 'Moderate Breeze'),
        (FreshBreeze, 'Fresh Breeze'),
        (StrongBreeze, 'Strong Breeze'),
        (NearGale, 'Near Gale'),
        (Gale, 'Gale'),
        (SevereGale, 'Severe Gale'),
        (Storm, 'Storm')
    )

    windlevel = models.IntegerField(choices=WindLevel)
    locations = models.MultiPolygonField()
    objects = models.GeoManager()
