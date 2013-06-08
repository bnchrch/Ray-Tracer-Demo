#import sys
import math
#import time

#from Material import *
from Vector import *
#from Point import *
from reverseRay import *
#from Plane import *
#from Sphere import *
#from raytrace import *
#from World import *
#from Image import *


#combine two colors and a coefficient
def combine(a, scale, initialColor):
    return (a[0] + scale * initialColor[0],
            a[1] + scale * initialColor[1],
            a[2] + scale * initialColor[2])

class Material:
    def __init__(self, color):
        self.Color = color
        self.specular = 0.2
        self.difuse = 0.6
        self.ambient = 0.2
    
    
    
    def getPixelColor(self, world, ray, curPoint, normal):
        initialColor = self.Color
        #light color
        finalColor = (0,0,0)

        #SPECULAR START
        #get the reflection of the ray by the normal
        reflected = ray.vector.Reflect(normal)

        #create a reflected ray
        reflectedRay = reverseRay(curPoint, reflected)
        
        #find the ray color of the reflected ray
        reflectedColor = world.rayColor(reflectedRay)

        #get reflected ray until hits nothing
        finalColor = combine(finalColor, self.specular, reflectedColor)
        #SPECULAR END

        #DIFUSE START
       
        difusePower = 0

        #this is the portion that does shadows
        #visibleLights = []
        flag=True
        
        #find if the light intersects any of the objects
        for (obj, material) in world.objectArray:
            lightRay = reverseRay(curPoint,world.lightPoint - curPoint)
            isIntersect = obj.intersection(lightRay)
            if isIntersect is not None and isIntersect > 0.00001:
                flag=False

        #if a light intersects the object and the current point
        #add the difuse
        #helps create soft shadows
        if flag:
            contribution = (world.lightPoint - curPoint).normalized().dot(normal)
            if contribution > 0:
                difusePower = difusePower + 1.5*contribution
        flag = True


    
        #cap the diffuse power
        difusePower = min(1,difusePower)


        finalColor = combine(finalColor, self.difuse * difusePower, initialColor)
        #DIFUSE END


        #AMBIENT START
        #combine the ambient into the color
        finalColor = combine(finalColor, self.ambient, initialColor)
        #AMBIENT End
    
        return finalColor
