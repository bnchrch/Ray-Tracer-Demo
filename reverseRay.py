
import math


from Vector import *

#ray class
class reverseRay:
    def __init__(self, point, vector):
        self.point = point
        self.vector = vector.normalized()
    

    #position of ray at time t
    def Position(self, t):
        return self.point + (self.vector*t)