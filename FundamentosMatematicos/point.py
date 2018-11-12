from math import sqrt
class Point:
    def __init__(self,x_init,y_init):
        self.x = x_init
        self.y = y_init
        self.angle = 0.0

    def shift(self, x, y):
        self.x += x
        self.y += y

    def __lt__(self,p):
        if(self.x<p.x):
            retorno = self
        else:
            if(self.x == p.x):
                if(self.y<p.x):
                    retorno = self
                else:
                    retorno = p
            else:
                retorno = p
        return retorno

    def __repr__(self):
        return "".join(["Point(", str(self.x), ",", str(self.y), "), -> Angle: ",str(self.angle)])
def distance(a, b):
    return sqrt((a.x-b.x)**2+(a.y-b.y)**2)


