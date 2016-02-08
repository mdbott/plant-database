from django.db import models

# Create your models here.
# Mineral Class Definitions
#
# This arrangement allows the enumeration of the minerals that
# each plant requires or provides


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


class LightLevel(models.Model):
    FULLSUN = 3
    PARTIALSHADE = 2
    DEEPSHADE = 1
    CATEGORIES = (
            (FULLSUN, 'Full Sun'),
            (PARTIALSHADE, 'Partial Shade'),
            (DEEPSHADE, 'Deep Shade'),
        )
    lightLevels = dict(CATEGORIES)
    intensity = models.IntegerField(choices=CATEGORIES, blank=True, null=True)
    description = models.CharField(max_length=50, blank=True)

    def __unicode__(self):
        return "%s" % self.description

    class Meta:
        verbose_name = 'Light Level'
        verbose_name_plural = 'Light Levels'
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
    legacy_pfaf_latin_name = models.CharField(max_length=200, blank=True, null=True)
    family = models.CharField(max_length=100, blank=True, null=True)
    genus = models.CharField(max_length=100, blank=True, null=True)
    hybrid = models.CharField(max_length=100, blank=True, default='', null=True)
    species = models.CharField(max_length=100, blank=True, null=True)
    ssp = models.CharField(max_length=100, blank=True, null=True)
    common_name = models.CharField(max_length=100, blank=True, null=True)
    habitat = models.CharField(max_length=1024, blank=True, null=True)
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
    lightInteraction = models.ManyToManyField(LightLevel, blank=True, through='LightInteraction')
    cultivation_details = models.TextField(max_length=10024, blank=True, null=True)
    propagation_details = models.ManyToManyField(Propagation, blank=True, through='PropagationDetails')
    known_hazards = models.TextField(blank=True, null=True)

    # class Meta:
    #    unique_together = ('family' , 'genus' , 'species' , 'ssp')

    def __unicode__(self):
        return "%s" % self.legacy_pfaf_latin_name


class SoilProperty(models.Model):
    PROPERTY_TYPE_CHOICES = (('pH', 'pH'), ('moisture', 'moisture'), ('Fertility', 'Fertility'),
                             ('Texture', 'Texture'), )
    name = models.CharField(max_length=30, blank=True)
    type = models.CharField(max_length=20, choices=PROPERTY_TYPE_CHOICES)
    description = models.CharField(max_length=100, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Soil Properties"

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


class Rootstock(models.Model):
    name = models.CharField(max_length=100, default='Base Rootstock')
    notes_on_rootstock = models.TextField(blank=True, null=True)
    plant = models.ForeignKey(Plant)
    height = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2)
    width = models.DecimalField(blank=True, null=True, max_digits=4, decimal_places=2)
    growth_rate = models.CharField(max_length=1, blank=True, default='M', null=True)
    # drought             = models.BooleanField(default=False)
    # acid_tolerance      = models.BooleanField(default=False)
    # alkaline_tolerance  = models.BooleanField(default=False)
    # saline_tolerance    = models.BooleanField(default=False)
    # sandy_soil          = models.BooleanField(default=True) # Equivalent to 'L' light in pfaf soil rating
    # loamy_soil          = models.BooleanField(default=True) # Equivalent to 'M' medium in pfaf soil rating
    # clay_soils          = models.BooleanField(default=True) # Equivalent to 'H' heavy in pfaf soil rating
    # poor_soil           = models.BooleanField(default=False)
    # acid_soils          = models.BooleanField(default=True) # Equivalent to 'A' acid in pfaf ph rating
    # neutral_soils       = models.BooleanField(default=True) # Equivalent to 'N' neutral in pfaf ph rating
    # basic_soils         = models.BooleanField(default=True) # Equivalent to 'B' basic in pfaf ph rating
    # moisture            = models.CharField(max_length=3, blank=True,default='M')
    soilinteractions = models.ManyToManyField(SoilProperty, blank=True, through='SoilRelation')

    class Meta:
        unique_together = ('name', 'plant')


class ReferenceList(models.Model):
    title = models.CharField(max_length=30, blank=True, null=True)
    author = models.CharField(max_length=100, blank=True, null=True)
    comments = models.CharField(max_length=30, blank=True, null=True)
    publisher = models.CharField(max_length=100, blank=True, null=True)
    publication_date = models.DateTimeField(blank=True, null=True)
    isbn = models.CharField(max_length=100, blank=True, null=True)


# Soil Relation Tables for the each Rootstock

class SoilRelation(models.Model):

    CATEGORIES = (
        ('Requires', 'Requires'),
        ('Provides', 'Provides'),
        ('Tolerates', 'Tolerates'),
        ('Cannot Tolerate', 'Cannot Tolerate'))
    RATING = (
            ('Low', 'Low'),
            ('Medium', 'Medium'),
            ('Large', 'Large'))

    rootstock = models.ForeignKey(Rootstock)
    soilProperty = models.ForeignKey(SoilProperty)
    relationType = models.CharField(max_length=20, choices=CATEGORIES, blank=True)
    relationIntensity = models.CharField(max_length=20, choices=RATING, blank=True)
    description = models.TextField(max_length=100, blank=True)

    class Meta:
        ordering = ['rootstock']


class EdibleType(models.Model):
    name = models.CharField(max_length=20, blank=True)

    def __unicode__(self):
        return self.name


class Cultivar(models.Model):
    name = models.CharField(max_length=100, default='Base Cultivar', blank=True)
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
    leaf_startmonth = models.IntegerField(blank=True, null=True)
    months_in_leaf = models.IntegerField(blank=True, null=True)
    flower_startmonth = models.IntegerField(blank=True, null=True)
    months_in_flower = models.IntegerField(blank=True, null=True)
    production_startmonth = models.IntegerField(blank=True, null=True)
    months_in_production = models.IntegerField(blank=True, null=True)
    seed_start_month = models.IntegerField(blank=True, null=True)
    months_seed_ripe = models.IntegerField(blank=True, null=True)
    # Equivalent to 'F' full shade in pfaf shade rating
    # semi_shade              = models.BooleanField(default=True)  # Equivalent to 'S' semi shade in pfaf shade rating
    # no_shade                = models.BooleanField(default=True)  # Equivalent to 'N' no shade in pfaf shade rating

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
class LightInteraction(models.Model):

    CATEGORIES = (
        ('Requires', 'Requires'),
        ('Provides', 'Provides'),
        ('Tolerates', 'Tolerates'),
        ('Cannot Tolerate', 'Cannot Tolerate'))

    plant = models.ForeignKey(Plant, related_name='light_entries')
    location = models.ForeignKey(LightLevel)
    relationType = models.CharField(max_length=20, choices=CATEGORIES, blank=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['plant']

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
