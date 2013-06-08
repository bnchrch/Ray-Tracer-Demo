
import math
import array
class Image:
    def __init__(self, width, height, name):
        #create byte array of size
        size = width * height
        self.bytes = array.array('B', [0] * (width * height * 3))
        for i in range(size):
            self.bytes[i * 3 + 2] = 255
        self.width = width
        self.height = height
        self.name = name

    def load(self, x, y, red, green, blue):
        i = ((self.height - y - 1) * self.width + x) * 3
        self.bytes[i] = max(0, min(255, int(red * 256)))
        self.bytes[i+1] = max(0, min(255, int(green * 256)))
        self.bytes[i+2] = max(0, min(255, int(blue * 256)))
    
    def toFile(self):
        with open(self.name, 'wb') as fp:
            fp.write('P6 %d %d 255\n' % (self.width, self.height))
            fp.write(self.bytes.tostring())