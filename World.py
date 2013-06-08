import sys
import math
import time

#from Material import *
from Vector import *

#of all the intersections the ray makes on object,
# find the one with the shortest distanct
def firstIntersection(intersections):
    closest = None
    for hit in intersections:
        hold = hit[1]
        if hold > -0.00001:
            if closest is None or hold < closest[1]:
                closest = hit
    return closest

class World:
    def __init__(self, rec):
        self.objectArray = []
        self.lightPoint = Point(25, 25, 10)
        self.position = Point(0, 2, 15)
        self.eyeDirection = Point(0,3,-1) #looking position
        self.bgColor = (1,1,1)
        self.recDepth = 0
        self.maxDepth = rec
    
    def add(self, object, material):
        self.objectArray.append((object, material))
    
    
    #where inter sections are computed
    def rayColor(self, ray):
        intersections = []
        #if the recursion depth is exceeded stop
        if self.recDepth > self.maxDepth:
            return self.bgColor

        try:
            self.recDepth = self.recDepth + 1

            #find all intersections
            for (obj, material) in self.objectArray:
                intersect = obj.intersection(ray)
                if intersect is not None:
                    intersections.append((obj, intersect, material))

            #get the closest intersection
            hit = firstIntersection(intersections)

            #if there are none then you've gone as far as possible
            #return white
            if hit is None:
                return self.bgColor ## the background color

            #find the position of the ray at the certain time
            #get the normal and get the pixel color
            #note this with recursively call this
            else:
                #(obj, t, material) = i
                posAtTime = ray.Position(hit[1])
                normal = hit[0].getNormal(posAtTime)
                return hit[2].getPixelColor(self, ray, posAtTime, normal)
        finally:
            self.recDepth = self.recDepth - 1
