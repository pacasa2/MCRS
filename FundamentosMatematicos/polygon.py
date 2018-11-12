from math import sqrt
from math import atan2
from point import Point

def angulo (p):
    return p.angulo
class Polygon:
    def __init__(self):
        self.points = list()
        self._initPoint= Point(0,0)
    def add(self, p):
        self.points.append(p)
    def orderPointsByGraham(self):
        for i in self.points:
            i.angle = atan2(  i.y -self._initPoint.y ,i.x -  self._initPoint.x)
        orderedList =  sorted(self.points,key=lambda p:float(p.angle))
        orderedList.insert(0, orderedList.pop(orderedList.index(self._initPoint)))
        return orderedList
    def initPoint(self):
        lower = self.points[0]
        for j in self.points:
            if(j.y<=lower.y):
                if (j.x<lower.x):
                    lower = j
        return lower
    def __repr__(self):
        l = ''
        for p in self.points:
            l+=str(p)+'; '
        return l
