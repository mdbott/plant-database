from django.contrib import admin
from nested_admin import NestedStackedInline, TabularInline, NestedAdmin
from .models import Plant, Cultivar, Rootstock, SoilRelation, MineralInteraction, LocationInteraction, Edible
from .models import Mineral, SoilProperty, PlantLocation, ReferenceList, EdibleType, LightLevel, LightInteraction


class SoilRelationInline(TabularInline):
    model = SoilRelation
    list_display = ('rootstock', 'relationtype', 'description')
    extra = 1


class RootstockStackedInline(NestedStackedInline):
    model = Rootstock
    inlines = [SoilRelationInline, ]
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

class LightInteractionStackedInline(TabularInline):
    model = LightInteraction
    extra = 1

class PlantAdmin(NestedAdmin):
    list_display = ('genus', 'species', 'ssp', 'common_name')
    inlines = [MineralInteractionStackedInline, LocationInteractionStackedInline, CultivarStackedInline,
               RootstockStackedInline, LightInteractionStackedInline]


admin.site.register(Plant, PlantAdmin)


class SoilPropertyAdmin(admin.ModelAdmin):
    ordering = ['type']

admin.site.register(SoilProperty, SoilPropertyAdmin)


class MineralAdmin(admin.ModelAdmin):
    ordering = ['name']

admin.site.register(Mineral, MineralAdmin)


class PlantLocationAdmin(admin.ModelAdmin):
    ordering = ['location']


admin.site.register(PlantLocation, PlantLocationAdmin)


class LightAdmin(admin.ModelAdmin):
    ordering = ['description']


admin.site.register(LightLevel, LightAdmin)


class ReferenceListAdmin(admin.ModelAdmin):
    ordering = ['title']

admin.site.register(ReferenceList, ReferenceListAdmin)


class EdibleTypeAdmin(admin.ModelAdmin):
    ordering = ['name']

admin.site.register(EdibleType, EdibleTypeAdmin)
