# from django.contrib import admin
from django import forms
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.gis import admin
from nested_admin import NestedStackedInline, TabularInline, NestedAdmin
from .models import Plant, Cultivar, Rootstock, MineralInteraction, LocationInteraction, Edible, \
    RootPathogenResistance, Usage, Medicinal, MedicinalUse
from .models import Mineral, PlantLocation, EdibleUse, RootPathogen, Vegetation, MoistureZone, \
    SalinityZone, pHZone, WindZone, ColourTest, PlantUse, References, ReferenceDetail


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
    list_display = ('plant', 'edible_use', 'edibility_rating')
    extra = 1


class MedicinalInline(TabularInline):
    model = Medicinal
    list_display = ('plant', 'medicinal_use', 'medicinal_rating')
    extra = 1


class CultivarStackedInline(NestedStackedInline):
    model = Cultivar
    inlines = [EdibleInline, MedicinalInline]
    extra = 0


class PlantUsageStackedInline(TabularInline):
    model = Usage
    extra = 1


class MineralInteractionStackedInline(TabularInline):
    model = MineralInteraction
    extra = 1


class LocationInteractionStackedInline(TabularInline):
    model = LocationInteraction
    extra = 1


class ReferenceDetailStackedInline(TabularInline):
    model = ReferenceDetail
    extra = 1

# class LightInteractionStackedInline(TabularInline):
#     model = LightInteraction
#     extra = 1


class PlantAdmin(NestedAdmin):
    list_display = ('genus', 'species', 'ssp', 'common_name')
    inlines = [MineralInteractionStackedInline, LocationInteractionStackedInline, PlantUsageStackedInline,
               CultivarStackedInline, RootstockStackedInline, ReferenceDetailStackedInline]


admin.site.register(Plant, PlantAdmin)

admin.site.register(ColourTest, admin.ModelAdmin)
# class SoilPropertyAdmin(admin.ModelAdmin):
#     ordering = ['use']
#
# admin.site.register(SoilProperty, SoilPropertyAdmin)


class RootPathogenAdmin(admin.ModelAdmin):
    ordering = ['name']

admin.site.register(RootPathogen, RootPathogenAdmin)


class MineralAdmin(admin.ModelAdmin):
    ordering = ['name']


admin.site.register(Mineral, MineralAdmin)


class PlantUseAdmin(admin.ModelAdmin):
    ordering = ['use']


admin.site.register(PlantUse, PlantUseAdmin)


class PlantLocationAdmin(admin.ModelAdmin):
    ordering = ['location']


admin.site.register(PlantLocation, PlantLocationAdmin)


# class ReferenceListAdmin(admin.ModelAdmin):
#     ordering = ['title']
#
# admin.site.register(ReferenceList, ReferenceListAdmin)


class ReferenceAdmin(admin.ModelAdmin):
    ordering = ['title']

admin.site.register(References, ReferenceAdmin)


class EdibleUseAdmin(admin.ModelAdmin):
    ordering = ['use']

admin.site.register(EdibleUse, EdibleUseAdmin)


class MedicinalUseAdmin(admin.ModelAdmin):
    ordering = ['use']

admin.site.register(MedicinalUse, MedicinalUseAdmin)


class VegetationAdminForm(forms.ModelForm):
    class Meta:
        model = Vegetation
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(VegetationAdminForm, self).__init__(*args, **kwargs)
        if self.instance and self.has_related_plant():
            self.fields['rootstock'].queryset = Rootstock.objects.filter(plant=self.instance.plant)
            self.fields['cultivar'].queryset = Cultivar.objects.filter(plant=self.instance.plant)

    def has_related_plant(self):
        has_plant = False
        try:
            has_plant = (self.instance.plant is not None)
        except ObjectDoesNotExist:
            pass
        return has_plant


class VegetationAdmin(admin.OSMGeoAdmin):
    form = VegetationAdminForm

    def save_model(self, request, obj, form, change):
        if not change:
            obj.rootstock = Rootstock.objects.filter(plant=obj.plant, base_rootstock=True).first()
            obj.cultivar = Cultivar.objects.filter(plant=obj.plant, base_cultivar=True).first()
        obj.save()

admin.site.register(Vegetation, VegetationAdmin)

admin.site.register(MoistureZone, admin.OSMGeoAdmin)

admin.site.register(SalinityZone, admin.OSMGeoAdmin)

admin.site.register(pHZone, admin.OSMGeoAdmin)

admin.site.register(WindZone, admin.OSMGeoAdmin)
