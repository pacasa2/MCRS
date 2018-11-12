from math import fabs
from point import Point
from polygon import Polygon
import pygame # necesito instalarlo: desde una linea de comandos -> pip install pygame

#Global Variables
size = [800, 600]
GREEN = (  0, 255,   0)
RED = (  255, 0,   0)
BLUE = (  0, 0,   255)

# DEFINE AND ADD POINT LIST
#Polygon 1 
poly1 = Polygon()
poly1_p1 = Point(30,30)
poly1_p2 = Point(400,50)
poly1_p3 = Point(600,200)
poly1_p4 = Point(400,300)
poly1_p5 = Point(600,400)
poly1_p6 = Point(200,300)
poly1_p7 = Point(300,200)
poly1.add(poly1_p1)
poly1.add(poly1_p2)
poly1.add(poly1_p3)
poly1.add(poly1_p4)
poly1.add(poly1_p5)
poly1.add(poly1_p6)
poly1.add(poly1_p7)
#Polygon 2
poly2 = Polygon()
poly2_p1 = Point(150,500)
poly2_p2 = Point(250,500)
poly2_p3 = Point(200,450)
poly2_p4 = Point(200,450)
poly2_p5 = Point(60,400)
poly2.add(poly2_p1)
poly2.add(poly2_p2)
poly2.add(poly2_p3)
poly2.add(poly2_p4)
poly2.add(poly2_p5)

#Polygon 3
poly3 = Polygon()
poly3_p1 = Point(600,450)
poly3_p2 = Point(650,370)
poly3_p3 = Point(700,450)
poly3_p4 = Point(650,500)
poly3.add(poly3_p1)
poly3.add(poly3_p2)
poly3.add(poly3_p3)
poly3.add(poly3_p4)

#Polygon 4
poly4 = Polygon()
poly4_p1 = Point(450,350)
poly4_p2 = Point(550,450)
poly4_p3 = Point(550,350)
poly4_p4 = Point(450,450)
poly4.add(poly4_p1)
poly4.add(poly4_p2)
poly4.add(poly4_p3)
poly4.add(poly4_p4)

#---------------------------------------------------------------------
#Returns Axis Align Bounding Box for a given polygon. Returns a struct with Center (x,y) and HalfExtents of Box
#---------------------------------------------------------------------*/
def findAABB (points):
    max_x = points[0].x
    max_y = points[0].y
    min_x = points[0].x
    min_y = points[0].y
    aabb_center = Point(0,0)
    aabb_halfExtents = Point(0,0)
    for point in points:
        if(point.x < min_x):
            min_x = point.x 
        elif(point.x>max_x):
            max_x = point.x
        if(point.y < min_y):
            min_y = point.y 
        elif(point.y>max_y):
            max_y = point.y
    aabb_center.x = (max_x+min_x)/2
    aabb_center.y = (max_y+min_y)/2
    aabb_halfExtents.x = fabs((max_x-min_x)/2)
    aabb_halfExtents.y = fabs((max_y-min_y)/2)
    return {'center':aabb_center,'halfExtents':aabb_halfExtents}
aabb = findAABB(poly1.points)
aabb2 = findAABB(poly2.points)
aabb3 = findAABB(poly3.points)
aabb4 = findAABB(poly4.points)

#DRAW FUNCTIONS

#---------------------------------------------------------------------
#Draws a set of Pygame lines from a list of points defyning a polygon
#---------------------------------------------------------------------*/
def drawPolygon (originalPoints):
    for i in range(0,len(originalPoints)-1):
        pygame.draw.line(screen, GREEN, [originalPoints[i].x,(size[1] - originalPoints[i].y)], [originalPoints[i+1].x,( size[1] -originalPoints[i+1].y)], 3)
        if i==(len(originalPoints)-2):
            pygame.draw.line(screen, GREEN, [originalPoints[i+1].x,(size[1] - originalPoints[i+1].y)], [originalPoints[0].x,( size[1] -originalPoints[0].y)], 3)
#---------------------------------------------------------------------
#Draws an AABB with Pygame Lines
#---------------------------------------------------------------------*/
def drawAABB (aabb):
    #DRAW AABB 
    pygame.draw.line(screen, BLUE, [(aabb['center'].x-aabb['halfExtents'].x),size[1]-(aabb['center'].y-aabb['halfExtents'].y)],[(aabb['center'].x+aabb['halfExtents'].x),size[1]-(aabb['center'].y-aabb['halfExtents'].y)] , 1)
    pygame.draw.line(screen, BLUE, [(aabb['center'].x-aabb['halfExtents'].x),size[1]-(aabb['center'].y+aabb['halfExtents'].y)],[(aabb['center'].x+aabb['halfExtents'].x),size[1]-(aabb['center'].y+aabb['halfExtents'].y)] , 1)
    pygame.draw.line(screen, BLUE, [(aabb['center'].x+aabb['halfExtents'].x),size[1]-(aabb['center'].y-aabb['halfExtents'].y)],[(aabb['center'].x+aabb['halfExtents'].x),size[1]-(aabb['center'].y+aabb['halfExtents'].y)] , 1)
    pygame.draw.line(screen, BLUE, [(aabb['center'].x-aabb['halfExtents'].x),size[1]-(aabb['center'].y-aabb['halfExtents'].y)],[(aabb['center'].x-aabb['halfExtents'].x),size[1]-(aabb['center'].y+aabb['halfExtents'].y)] , 1)
#---------------------------------------------------------------------
#Returns TRUE if AABB's a and b intersect
#---------------------------------------------------------------------*/
def aabbIntersect(a, b):
    return (fabs(a['center'].x - b['center'].x) < (a['halfExtents'].x + b['halfExtents'].x)) and (fabs(a['center'].y - b['center'].y) < (a['halfExtents'].y + b['halfExtents'].y))


print("aabb y aabb2 intersectan?: "+ str(aabbIntersect(aabb,aabb2)))
print("aabb y aabb3 intersectan?: "+ str(aabbIntersect(aabb,aabb3)))
print("aabb y aabb4 intersectan?: "+ str(aabbIntersect(aabb,aabb4)))
print("aabb3 y aabb4 intersectan?: "+ str(aabbIntersect(aabb3,aabb4)))

#PyGame Drawing Loop
pygame.init()
screen = pygame.display.set_mode(size)
running = True
while running: # This would start the event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # This would be a quit event.
            running = False # So the user can close the program
    drawPolygon(poly1.points) #Draw Polygon1
    drawPolygon(poly2.points) #Draw Polygon2
    drawPolygon(poly3.points) #Draw Polygon3
    drawPolygon(poly4.points) #Draw Polygon4
    drawAABB(aabb) #Draw Polygon1 AABB
    drawAABB(aabb2) #Draw Polygon2 AABB
    drawAABB(aabb3) #Draw Polygon3 AABB
    drawAABB(aabb4) #Draw Polygon4 AABB
    pygame.display.flip() # This "flips" the display so that it shows something
pygame.quit()
