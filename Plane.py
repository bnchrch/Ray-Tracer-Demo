import sys
import math

from Vector import *

#plane object
class Plane:
    def __init__(self):
        self.point = Point(0,0,0)
        self.normal = Vector(0,1,0)

    #intersection
    #if the vector intersects return it's reflection direction
    def intersection(self, ray):
        v = ray.vector.dot(self.normal)
        if v:
            return 1 / -v
        else:
            return None

    def getNormal(self, p):
        return self.normal