from math import sqrt
from point import Point
class Vector:
    def __init__(self,x_init,y_init):
        self.x = x_init
        self.y = y_init

    def length(self):
        return sqrt(self.x**2+self.y**2)
    
    def dot(self, v2):
        return (self.x*v2.x) +(self.y*v2.y)

    def __repr__(self):
        return "".join(["Vector(", str(self.x), ",", str(self.y), ")"])

v1 = Vector (6,5)
v2 = Vector(3,7)
v1_len = v1.length()
dottie = v1.dot(v2)
print(v1_len)
print(dottie)
print (v1)