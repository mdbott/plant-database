# from django.contrib import admin
from django import forms
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.gis import admin
from nested_admin import NestedStackedInline, TabularInline, NestedAdmin
from .models import Plant, Cultivar, Rootstock, MineralInteraction, LocationInteraction, Edible, \
    RootPathogenResistance, Usage, Medicinal, MedicinalUse, CultivarImage
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


class CultivarImageInline(TabularInline):
    model = CultivarImage
    extra = 1

    fields = ('image_tag', 'picture', 'caption', )
    readonly_fields = ('image_tag',)


class CultivarAdminForm(forms.ModelForm):
    class Meta:
        model = Vegetation
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CultivarAdminForm, self).__init__(*args, **kwargs)
        if self.instance and self.has_related_plant():
            self.fields['native_rootstock'].queryset = Rootstock.objects.filter(plant=self.instance.plant)

    def has_related_plant(self):
        has_plant = False
        try:
            has_plant = (self.instance.plant is not None)
        except ObjectDoesNotExist:
            pass
        return has_plant


class CultivarStackedInline(NestedStackedInline):
    form = CultivarAdminForm
    model = Cultivar
    inlines = [EdibleInline, MedicinalInline, CultivarImageInline]
    extra = 0

    def save_model(self, request, obj, form, change):
        if not change:
            obj.native_rootstock = Rootstock.objects.filter(plant=obj.plant, base_rootstock=True).first()
        obj.save()


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
            # self.fields['rootstock'].queryset = Rootstock.objects.filter(plant=self.instance.plant)
            self.fields['cultivar'].queryset = Cultivar.objects.filter(plant=self.instance.plant)
            self.fields['cultivar'].value = Cultivar.objects.filter(plant=self.instance.plant).first()

            if self.instance.grafted:
                self.fields['rootstock'].queryset = Rootstock.objects.filter(plant=self.instance.plant)
                self.fields['rootstock'].value = Rootstock.objects.filter(plant=self.instance.plant).first()
            else:
                # rootstock_ids = Cultivar.objects.filter(plant=self.instance.plant).values_list('native_rootstock_id')
                native_rootstock_id = self.instance.cultivar.native_rootstock.id
                self.fields['rootstock'].queryset = Rootstock.objects.filter(id=native_rootstock_id)
                self.fields['rootstock'].value = Rootstock.objects.filter(id=native_rootstock_id)
            # if self.instance.grafted:
            #     del self.fields['rootstock']

    def has_related_plant(self):
        has_plant = False
        try:
            has_plant = (self.instance.plant is not None)
        except ObjectDoesNotExist:
            pass
        return has_plant

    def clean_rootstock(self):
        if not self.instance.grafted:
            try:
                return self.instance.rootstock
            except ObjectDoesNotExist:
                return self.cleaned_data.get('rootstock')
        else:
            return self.cleaned_data.get('rootstock')

    def getnewfield(self):
        if self.instance.grafted:
            newfields = [
                ('rootstock', forms.CharField()),
                ('test2', forms.ModelMultipleChoiceField(Vegetation.objects.all(), widget=forms.CheckboxSelectMultiple)),
            ]
        else:
            newfields = {}
        return newfields


class VegetationAdmin(admin.OSMGeoAdmin):
    form = VegetationAdminForm

    def save_model(self, request, obj, form, change):
        if not change:
            obj.rootstock = Rootstock.objects.filter(plant=obj.plant, base_rootstock=True).first()
            obj.cultivar = Cultivar.objects.filter(plant=obj.plant, base_cultivar=True).first()
        if change and 'plant' in form.changed_data:
            obj.rootstock = Rootstock.objects.filter(plant=obj.plant, base_rootstock=True).first()
            obj.cultivar = Cultivar.objects.filter(plant=obj.plant, base_cultivar=True).first()
        if change and ('grafted' in form.changed_data or 'cultivar' in form.changed_data) and obj.grafted is False:
            native_rootstock_id = obj.cultivar.native_rootstock.id
            obj.rootstock = Rootstock.objects.filter(id=native_rootstock_id).first()
        obj.save()

    def get_fields(self, request, obj=None):
        gf = super(VegetationAdmin, self).get_fields(request, obj)
        adminform = VegetationAdminForm()
        new_dynamic_fields = self.form.getnewfield(VegetationAdminForm())
        if VegetationAdminForm().getnewfield():

            # without updating get_fields, the admin form will display w/o any new fields
            # without updating base_fields or declared_fields, django will throw an error: django.core.exceptions.FieldError: Unknown field(s) (test) specified for MyModel. Check fields/fieldsets/exclude attributes of class MyModelAdmin.

            for f in new_dynamic_fields:
                # `gf.append(f[0])` results in multiple instances of the new fields
                #gf = gf + [f[0]]
                # updating base_fields seems to have the same effect
                self.form.declared_fields.update({f[0]: f[1]})
        return gf
    # def get_fieldsets(self, request, obj=None):
    #     fieldsets = super(VegetationAdmin, self).get_fieldsets(request, obj)
    #     fieldsets[0][1]['fields'] += ('foo', )
    #     return fieldsets
    #
    # def get_form(self, request, obj=None, **kwargs):
    #     adminform = VegetationAdminForm()
    #     fields = adminform.getnewfield()
    #     form = type('VegetationAdminForm', (forms.ModelForm,), fields)
    #     return form

admin.site.register(Vegetation, VegetationAdmin)

admin.site.register(MoistureZone, admin.OSMGeoAdmin)

admin.site.register(SalinityZone, admin.OSMGeoAdmin)

admin.site.register(pHZone, admin.OSMGeoAdmin)

admin.site.register(WindZone, admin.OSMGeoAdmin)
