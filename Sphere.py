#import sys
import math

from Vector import *

#
#Sphere object for raytracer
#
class Sphere:
    def __init__(self, centre, radius):
        #centre.mustBePoint()
        self.centre = centre
        self.radius = radius
    
    #find out if the ray intersects the sphere
    # return nothing if it does or return the time it takes for the ray to reach the sphere if so
    def intersection(self, ray):

        #calculate the discriminant
        #if < 0 the ray did not intersect the sphere

        centerPoint = self.centre - ray.point
        lengthCP = centerPoint.dot(centerPoint)
        rad2 = math.pow(self.radius, 2)
        t = centerPoint.dot(ray.vector)
        disc = rad2 - (lengthCP - math.pow(t,2))
        if disc < 0:
            return None
        else:

            #returns the time needed to intersect the sphere
            return t - math.sqrt(disc)

    #returns the normal from the sphere to the point
    def getNormal(self, p):
        return (p - self.centre).normalized()