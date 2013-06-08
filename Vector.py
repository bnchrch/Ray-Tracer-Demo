
import math

#point class
	#add
	#sub
	#mul
class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __add__(self, a):
        x = self.x + a.x
        y = self.y + a.y
        z = self.z + a.z

        return Point(x, y, z)
       
    
    def __sub__(self, a):
        x = self.x - a.x
        y = self.y - a.y
        z = self.z - a.z

        if a.checkPoint():
            return Vector(x, y, z)
        else:
            return Point(x, y, z)

    def __mul__(self, a):
        return Point(self.x*a, self.y * a, self.z * a)

    
    def checkPoint(self):
        return True
        
#vector class
	#eq
	#add
	#sub
	#mul
	#dot
	#cross
	#normalize
	#reflect
class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __eq__(self, a):
        return (self.x == a.x) and (self.y == a.y) and (self.z == a.z)

    def __add__(self, a):
        if a.checkPoint():
            return Point(self.x + a.x, self.y + a.y, self.z + a.z)
        else:
            return Vector(self.x + a.x, self.y + a.y, self.z + a.z)
    
    def __sub__(self, a):
        
        return Vector(self.x - a.x, self.y - a.y, self.z - a.z)

    def __mul__(self, a):
     
        return Vector(self.x*a, self.y * a, self.z * a)


    def dot(self, a):
       
        return (self.x * a.x) + (self.y * a.y) + (self.z * a.z)

    def cross(self, a):
       
        return Vector(self.y * a.z - self.z * a.y,
                      self.z * a.x - self.x * a.z,
                      self.x * a.y - self.y * a.x)

    def normalized(self):
        return self*(1.0 / math.sqrt(self.dot(self)))

    
    def Reflect(self, normal):
        d = normal*(2*self.dot(normal))
        return self - d
  
    def checkPoint(self):
        return False