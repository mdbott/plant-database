# from django.db import models
from django.contrib.gis.db import models
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
        defaults = {'min_value': self.min_value, 'max_value' : self.max_value}
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


class Plant(models.Model):
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

    FullSun = 3
    PartialShade = 2
    DeepShade = 1
    LightLevel = (
            (FullSun, 'Full Sun'),
            (PartialShade, 'Partial Shade'),
            (DeepShade, 'Deep Shade'),
        )

    # Plant Uses
    Productive = 1
    Support = 2
    Weed = 3
    Native = 4
    Uses = (
        (Productive, 'Productive Species'),
        (Support, 'Support Species'),
        (Weed, 'Weed/Volunteer Species'),
        (Native, 'Native Species')
    )
    # Plant Form
    LargeTree = 1
    MediumTree = 2
    SmallTree = 3
    Shrub = 4
    ProstrateShrub = 5
    Vine = 6
    Herbaceous = 7
    Form = (
        (LargeTree, 'Large Tree'),
        (MediumTree, 'Medium Tree'),
        (SmallTree, 'Small Tree'),
        (Shrub, 'Shrub'),
        (ProstrateShrub, 'Prostrate Shrub'),
        (Vine, 'Vine'),
        (Herbaceous, 'Herbaceous Species')
    )

    legacy_pfaf_latin_name = models.CharField(max_length=200, blank=True, null=True)
    family = models.CharField(max_length=100, blank=True, null=True)
    genus = models.CharField(max_length=100, blank=True, null=True)
    hybrid = models.CharField(max_length=100, blank=True, default='', null=True)
    species = models.CharField(max_length=100, blank=True, null=True)
    ssp = models.CharField(max_length=100, blank=True, null=True)
    common_name = models.CharField(max_length=100, blank=True, null=True)
    uses = models.IntegerField(blank=True, choices=Uses, null=True)
    form = models.IntegerField(blank=True, choices=Form, null=True)
    habitat = models.CharField(max_length=1024, blank=True, null=True)
    wind_lower_limit = models.IntegerField(blank=True, choices=WindLevel, null=True)
    wind_upper_limit = models.IntegerField(blank=True, choices=WindLevel, null=True)
    light_lower_limit = models.IntegerField(blank=True, choices=LightLevel, null=True)
    light_upper_limit = models.IntegerField(blank=True, choices=LightLevel, null=True)
    deciduous_evergreen = models.CharField(max_length=1024, blank=True, default='D', null=True)
    nitrogen_fixer = models.BooleanField(default=False)
    supports_wildlife = models.BooleanField(default=False)
    flower_type = models.CharField(max_length=2048, blank=True, default='N', null=True)
    pollinators = models.CharField(max_length=1024, blank=True, default='N', null=True)
    self_fertile = models.BooleanField(default=False)
    scented = models.CharField(max_length=1024, blank=True, default='N', null=True)
    pollution = models.BooleanField(default=False)
    mineralInteraction = models.ManyToManyField(Mineral, blank=True, through='MineralInteraction')
    locationInteraction = models.ManyToManyField(PlantLocation, blank=True, through='LocationInteraction')
    # lightInteraction = models.ManyToManyField(LightLevel, blank=True, through='LightInteraction')
    cultivation_details = models.TextField(max_length=10024, blank=True, null=True)
    propagation_details = models.ManyToManyField(Propagation, blank=True, through='PropagationDetails')
    known_hazards = models.TextField(blank=True, null=True)

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

    # name = models.CharField(max_length=20, choices=PROPERTY)
    # # models.IntegerField(blank=True, choices=INTPROPERTY)
    # description = models.CharField(max_length=100, blank=True)
    #
    # def __unicode__(self):
    #     return self.name
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
    MoistureLevel = (
        (Low, 'Low'),
        (Medium, 'Medium'),
        (High, 'High'),
    )
    name = models.CharField(max_length=100, default='Base Rootstock')
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
    # soilinteractions = models.ManyToManyField(SoilProperty, blank=True, through='SoilRequirement')
    # This will characterize soil interactions of the Plant with
    # - Soil Texture (Heavy, Medium)
    # - Salinity (High, Average, Low)
    # - Moisture Level ( Moist, Average, Dry)
    # - pH (Numeric)
    soildiseaseinteractions = models.ManyToManyField(RootPathogen, blank=True, through='RootPathogenResistance')

    def __unicode__(self):
        return self.name

    class Meta:
        unique_together = ('name', 'plant')

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


class ReferenceList(models.Model):
    title = models.CharField(max_length=30, blank=True, null=True)
    author = models.CharField(max_length=100, blank=True, null=True)
    comments = models.CharField(max_length=30, blank=True, null=True)
    publisher = models.CharField(max_length=100, blank=True, null=True)
    publication_date = models.DateTimeField(blank=True, null=True)
    isbn = models.CharField(max_length=100, blank=True, null=True)


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


class EdibleType(models.Model):
    name = models.CharField(max_length=20, blank=True)

    def __unicode__(self):
        return self.name


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
    name = models.CharField(max_length=100, default='Base Cultivar', blank=True)
    base_cultivar = models.BooleanField(default=False)
    notes_on_cultivar = models.TextField(blank=True, null=True)
    synonyms = models.TextField(blank=True, null=True)
    plant = models.ForeignKey(Plant)
    edible = models.ManyToManyField(EdibleType, blank=True, through='Edible')
    edibility_rating = models.IntegerField(blank=True, null=True)
    medicinal_rating = models.IntegerField(blank=True, null=True)
    wind_tolerance = models.IntegerField(blank=True, null=True)
    upperhardiness = models.IntegerField(default=0, blank=True, null=True)
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
    # Equivalent to 'F' full shade in pfaf shade rating
    # semi_shade              = models.BooleanField(default=True)  # Equivalent to 'S' semi shade in pfaf shade rating
    # no_shade                = models.BooleanField(default=True)  # Equivalent to 'N' no shade in pfaf shade rating

    def __unicode__(self):
        return self.name

    class Meta:
        unique_together = ('name', 'plant')


class Edible(models.Model):

    RATING = (
            ('Poor', 'Poor'),
            ('Fair', 'Fair'),
            ('Good', 'Good'),
            ('Excellent', 'Excellent'))

    plant = models.ForeignKey(Cultivar, related_name='plant_entries')
    edible_part = models.ForeignKey(EdibleType)
    ediblity_rating = models.CharField(max_length=20, choices=RATING, blank=True)
    edible_link = models.ManyToManyField(ReferenceList, blank=True, through='EdibleReference')
    notes = models.TextField(max_length=100, blank=True)

    class Meta:
        ordering = ['plant']


# Plant Mineral Relationship Class
class EdibleReference(models.Model):

    CATEGORIES = (
        ('Page Reference', 'Page Reference'),
        ('Website', 'Website'),
        ('Journal', 'Tolerates'))

    referenceLink = models.ForeignKey(ReferenceList)
    edible = models.ForeignKey(Edible)
    reference = models.CharField(max_length=20, choices=CATEGORIES, blank=True)
    notes = models.CharField(max_length=100, blank=True)

    class Meta:
        ordering = ['edible']


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
    description = models.TextField(blank=True)

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
    locations = models.PointField()
    comment = models.CharField(max_length=50, blank=True, null=False)
    germination_date = models.DateTimeField(blank=True, null=True)
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
