from django.db import models
from colorfield.fields import ColorField
from django import forms
from django.conf import settings


def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    result = '%s,%s,%s' % tuple(str(int(value[i:i + lv // 3], 16)) for i in range(0, lv, lv // 3))
    return result


def rgb_to_hex(rgb):
    values = tuple(map(int, rgb.split(',')))
    return '#%02x%02x%02x' % values


class RGBTuple(object):
    def __init__(self, red=0, green=0, blue=0):
        self.red = red
        self.green = green
        self.blue = blue

    def __repr__(self):
        return str(self.red) + ',' + str(self.green) + ',' + str(self.blue)


class HexColor(str):
    pass


class RGBColorField(ColorField):
    description = "A RGB Color Triplet"

    def __init__(self, help_text="A comma-separated red green blue triplet", *args, **kwargs):
        self.name = "RGBColorField",
        self.through = None
        self.help_text = help_text
        models.Field.creation_counter += 1
        super(RGBColorField, self).__init__(*args, **kwargs)

    def db_type(self, connection):
        return 'varchar(15)'

    def from_db_value(self, value, expression, connection, context):
        if value is None:
            return value
        return rgb_to_hex(value)

    def to_python(self, value):
        if isinstance(value, HexColor):
            return value

        if value is None:
            return value

        return value

    def get_prep_value(self, value):
        return hex_to_rgb(value)

    def get_internal_type(self):
        return 'CharField'

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return value




