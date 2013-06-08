import sys
import math
import time
import random

from Vector import *
from reverseRay import *
from Image import *
from Sphere import *
from World import *
from Plane import *
from Material import *

#print greeting message
def startingIntro(numSphere,depth, height, width, name, lightLoc):
    print '#####################'
    print 'Ray Tracer for csc305'
    print '#####################'
    print   ''
    print 'Spheres: '+str(numSphere) 
    print 'Recursion depth: '+str(depth)
    print 'Dimensions of image: '+str(width)+' x '+str(height)
    print 'Name of File: ' + name
    print ''
    print 'lets get started\n(be patient though the program will take a little time)'

if __name__ == '__main__':

    #if len(sys.argv) < 2:
     #   print 'Sorry you need to enter more arguments!\n The format is: Python raytrace [# of sp'
    
    numSphere = int(sys.argv[1])
    depth = int(sys.argv[2])
    
    #lay the frame work for my image file
    image = Image(500,400,'raytrace.ppm')

    #initialize the world
    world = World(depth)

    #create all spheres with a random color
    for offset in range(numSphere):
        sphere = Sphere(Point(-6 + (offset* 4), 3.4+ (offset%2), -5+(offset * 5)), 2)
        sphereColor = (
            1/float(random.randrange(1,5+1)),
            1/float(random.randrange(1,5+1)),
            1/float(random.randrange(1,5+1))
            )
        mat = Material(sphereColor)
        world.add(sphere, mat)

    #add plane
    world.add(Plane(), Material((0.1,0.3,0.4)))

    #print welcome message
    startingIntro(numSphere,depth, image.height, image.width, image.name, world.lightPoint)
    
    gaze = reverseRay(world.position, world.eyeDirection - world.position)
    cameraUP = gaze.vector.cross(Vector(0,1,0)).normalized()
    cameraDir = cameraUP.cross(gaze.vector).normalized()

    #compute field of view
    ratio =  float (image.height)/float(image.width)

    #45 degree field of view
    fieldRad = math.pi * (float(45) / float(2) / float(180))


    #get world dimensions
    width = (math.tan(fieldRad) * 2.0)
    height = ratio * math.tan(fieldRad) * 2.0
    pixelWidth = width / (image.width - 1)
    pixelHeight = height / (image.height - 1)
    
   #begin ray tracing
    for y in range(image.height):
        for x in range(image.width):
            xOffset = cameraUP*(x * pixelWidth - (width/2))
            yOffset = cameraDir*(y * pixelHeight - (height/2))
            #if x is 1 and y is 1:
             #   print xOffset.x, xOffset.y, xOffset.z
             #   print yOffset.x, yOffset.y, yOffset.z
            ray = reverseRay(gaze.point, gaze.vector + xOffset + yOffset)
            color = world.rayColor(ray)
            image.load(x,y,*color)

    print 'All done, look in this directory for ' + image.name


    image.toFile()