# Author: Kelvin Lai <kelvin@firststreet.org>
# Copyright: This module is owned by First Street Foundation

# Internal Imports
from shapely.geometry import shape


class Geometry:

    def __init__(self, geometry):

        if geometry:
            self.polygon = shape(geometry.get('polygon'))
            self.center = shape(geometry.get('center'))
            if geometry.get('bbox'):
                self.bbox = shape(geometry.get('bbox'))
            else:
                self.bbox = None

    def __eq__(self, other):
        if not isinstance(other, Geometry):
            return NotImplemented

        return self.polygon == other.polygon and self.center == other.center and self.bbox == other.bbox