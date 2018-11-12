from math import fabs
from point import Point
from polygon import Polygon
from tri import LeftOn
import pygame # necesito instalarlo: desde una linea de comandos -> pip install pygame

#Global Variables
size = [800, 600]
GREEN = (  0, 255,   0)
RED = (  255, 0,   0)
BLUE = (  0, 0,   255)

# DEFINE AND ADD POINT LIST
#Polygon 1 
p = Polygon()

p2 = Point(400,50)
p3 = Point(600,200)
p4 = Point(400,300)
p5 = Point(600,400)
p6 = Point(400,150)
p7 = Point(200,300)
p8 = Point(300,200)
p1 = Point(30,30)
p9 = Point(30,20)
p10 = Point(29,20)
p11 = Point(29,20)
p12 = Point(31,20)

p.add(p2)
p.add(p3)
p.add(p4)
p.add(p5)
p.add(p6)
p.add(p7)
p.add(p8)
p.add(p1)
p.add(p9)
p.add(p10)
p.add(p11)
p.add(p12)

poly2 = Polygon()

poly2_p1 = Point(300,500)
poly2_p2 = Point(250,600)
poly2_p3 = Point(200,500)
poly2.add(poly2_p1)
poly2.add(poly2_p2)
poly2.add(poly2_p3)




#find InitPoint
p._initPoint = p.initPoint()
print('INITIAL POINT Poly 1:  '+str(p._initPoint))
pointsOrdered = p.orderPointsByGraham()
print('ORDERGRAHAM Poly 1')
print(pointsOrdered)

#find InitPoint
poly2._initPoint = poly2.initPoint()
print('INITIAL POINT Poly 2:  '+str(poly2._initPoint))
pointsOrdered2 = poly2.orderPointsByGraham()
print('ORDERGRAHAM Poly 2')
print(pointsOrdered2)

print("####### COLOR CODE #######")
print("RED: ConvexHull")
print("GREEN: Polygon geometry")



#---------------------------------------------------------------------
#Returns Convex Hull of a given Polygon
#---------------------------------------------------------------------*/
def findConvexHullGraham(points):
    i = 2
    convexHull = list()
    convexHull.append(points[0])
    convexHull.append(points[1])
    while (i< (len(points))):
        if(LeftOn(convexHull[len(convexHull)-2],convexHull[len(convexHull)-1],points[i])):
            convexHull.append(points[i])
            i+=1
        else:
            convexHull.pop()
    return convexHull
convexHull = findConvexHullGraham(pointsOrdered)
convexHull2 = findConvexHullGraham(pointsOrdered2)
#DRAW FUNCTIONS

#---------------------------------------------------------------------
#Draws a set of Pygame lines from a list of points defyning a polygon
#---------------------------------------------------------------------*/
def drawPolygon (originalPoints):
    for i in range(0,len(originalPoints)-1):
        pygame.draw.line(screen, GREEN, [originalPoints[i].x,(size[1] - originalPoints[i].y)], [originalPoints[i+1].x,( size[1] -originalPoints[i+1].y)], 2)
        if i==(len(originalPoints)-2):
            pygame.draw.line(screen, GREEN, [originalPoints[i+1].x,(size[1] - originalPoints[i+1].y)], [originalPoints[0].x,( size[1] -originalPoints[0].y)], 2)
#---------------------------------------------------------------------
#Draws a set of Pygame lines from a list of points defyning a convex hull of a polygon
#---------------------------------------------------------------------*/ 
def drawConvexHull (convexHull):
    for i in range(0,len(convexHull)-1):
        pygame.draw.line(screen, RED, [convexHull[i].x,(size[1] - convexHull[i].y)], [convexHull[i+1].x,( size[1] -convexHull[i+1].y)], 5)
        if i==(len(convexHull)-2):
            pygame.draw.line(screen, RED, [convexHull[i+1].x,(size[1] - convexHull[i+1].y)], [convexHull[0].x,( size[1] -convexHull[0].y)], 5)

#PyGame Drawing Loop
pygame.init()
screen = pygame.display.set_mode(size)
running = True
while running: # This would start the event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # This would be a quit event.
            running = False # So the user can close the program
   
    drawConvexHull(convexHull) #Draw Polygon1 Convex Hull
    drawConvexHull(convexHull2) #Draw Polygon1 Convex Hull
    drawPolygon(p.points) #Draw Polygon1
    drawPolygon(poly2.points) #Draw Polygon2
   
    pygame.display.flip() # This "flips" the display so that it shows something
pygame.quit()
