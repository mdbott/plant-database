from django.contrib import admin
from nested_admin import NestedStackedInline, TabularInline, NestedAdmin
from .models import Plant, Cultivar, Rootstock, MineralInteraction, LocationInteraction, Edible, \
    RootPathogenResistance
from .models import Mineral, PlantLocation, ReferenceList, EdibleType, RootPathogen


# class SoilRequirementInline(TabularInline):
#     model = SoilRequirement
#     list_display = ('rootstock', 'relationtype', 'description')
#     extra = 1


class RootDiseaseResistanceInline(TabularInline):
    model = RootPathogenResistance
    list_display = ('rootstock', 'relationtype', 'description')
    extra = 1


class RootstockStackedInline(NestedStackedInline):
    model = Rootstock
    inlines = [RootDiseaseResistanceInline, ]
    extra = 0


class EdibleInline(TabularInline):
    model = Edible
    list_display = ('plant', 'edible_part', 'ediblity_rating')
    extra = 1


class CultivarStackedInline(NestedStackedInline):
    model = Cultivar
    inlines = [EdibleInline, ]
    extra = 0


class MineralInteractionStackedInline(TabularInline):
    model = MineralInteraction
    extra = 1


class LocationInteractionStackedInline(TabularInline):
    model = LocationInteraction
    extra = 1

# class LightInteractionStackedInline(TabularInline):
#     model = LightInteraction
#     extra = 1

class PlantAdmin(NestedAdmin):
    list_display = ('genus', 'species', 'ssp', 'common_name')
    inlines = [MineralInteractionStackedInline, LocationInteractionStackedInline, CultivarStackedInline,
               RootstockStackedInline]


admin.site.register(Plant, PlantAdmin)


# class SoilPropertyAdmin(admin.ModelAdmin):
#     ordering = ['name']
#
# admin.site.register(SoilProperty, SoilPropertyAdmin)

class RootPathogenAdmin(admin.ModelAdmin):
    ordering = ['name']

admin.site.register(RootPathogen, RootPathogenAdmin)

class MineralAdmin(admin.ModelAdmin):
    ordering = ['name']

admin.site.register(Mineral, MineralAdmin)


class PlantLocationAdmin(admin.ModelAdmin):
    ordering = ['location']


admin.site.register(PlantLocation, PlantLocationAdmin)


# class LightAdmin(admin.ModelAdmin):
#     ordering = ['description']
#
#
# admin.site.register(LightLevel, LightAdmin)


class ReferenceListAdmin(admin.ModelAdmin):
    ordering = ['title']

admin.site.register(ReferenceList, ReferenceListAdmin)


class EdibleTypeAdmin(admin.ModelAdmin):
    ordering = ['name']

admin.site.register(EdibleType, EdibleTypeAdmin)
