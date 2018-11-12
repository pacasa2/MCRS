#--------------------------------------------------------------------
#This code is described in "Computational Geometry in C" (Second Edition),
#Chapter 1.  It is not written to be comprehensible without the 
#explanation in that book.
#
#Input: 2n integer coordinates for vertices of a simple polygon,
#       in counterclockwise order.  NB: the code will not work
#       for points in clockwise order!
#Output: the diagonals of a triangulation, in PostScript.
#
#Compile: gcc -o tri tri.c (or simply: make)
#
#Written by Joseph O'Rourke, with contributions by Min Xu.
#Last modified: October 1997
#Questions to orourke@cs.smith.edu.
#--------------------------------------------------------------------
#This code is Copyright 1998 by Joseph O'Rourke.  It may be freely 
#redistributed in its entirety provided that this copyright notice is 
#not removed.
#--------------------------------------------------------------------

#---------------------------------------------------------------------
#Returns twice the signed area of the triangle determined by a,b,c.
#The area is positive if a,b,c are oriented ccw, negative if cw,
#and zero if the points are collinear.
#---------------------------------------------------------------------*/
def Area2( a,b,c):
    return (b.x - a.x) * (c.y - a.y) - (c.x - a.x) * (b.y - a.y)

def AreaSign( a, b, c):
    area2 = Area2(a,b,c)
    # The area should be an integer. #
    if area2 >  0.5 :
        return  1
    elif ( area2 < -0.5 ) :
        return -1
    else:
        return  0

#---------------------------------------------------------------------
#Exclusive or: TRUE iff exactly one argument is true.
#---------------------------------------------------------------------
def Xor(  x, y ):
    # The arguments are negated to ensure that they are 0/1 values. #
    # (Idea due to Michael Baldwin.) #
    return (not x) ^ (not y)


#---------------------------------------------------------------------
#Returns true iff ab properly intersects cd: they share
#a point interior to both segments.  The properness of the
#intersection is ensured by using strict leftness.
#---------------------------------------------------------------------*/
def IntersectProp(   a,  b,  c,  d ):
    # Eliminate improper cases. */
    if (Collinear(a,b,c) or Collinear(a,b,d) or Collinear(c,d,a) or Collinear(c,d,b)):
        return False

    return Xor( Left(a,b,c), Left(a,b,d) ) and Xor( Left(c,d,a), Left(c,d,b) )


#---------------------------------------------------------------------
#Returns true iff c is strictly to the left of the directed
#line through a to b.
#---------------------------------------------------------------------*/
def Left(  a,  b,  c ):
    return  AreaSign( a, b, c ) > 0

def	LeftOn(  a,  b,  c ):
    return  AreaSign( a, b, c ) >= 0

def	Collinear(   a,  b,  c ):
    return  AreaSign( a, b, c ) == 0
#---------------------------------------------------------------------
#Returns TRUE iff point c lies on the closed segement ab.
#First checks that c is collinear with a and b.
#---------------------------------------------------------------------*/
def	Between(   a,  b,  c ):
    if ( not Collinear( a, b, c ) ):
        return  False

    # If ab not vertical, check betweenness on x; else on y. */
    if ( a.x != b.x ) :
        return ((a.x <= c.x) and (c.x <= b.x)) or ((a.x >= c.x) and (c.x >= b.x))
    else:
        return ((a.y <= c.y) and (c.y <= b.y)) or ((a.y >= c.y) and (c.y >= b.y))


#---------------------------------------------------------------------
#Returns TRUE iff segments ab and cd intersect, properly or improperly.
#---------------------------------------------------------------------*/
def	Intersect(  a,  b,  c,  d ):
    if ( IntersectProp( a, b, c, d ) ):
        return  True
    elif (   Between( a, b, c ) or Between( a, b, d ) or Between( c, d, a ) or Between( c, d, b ) ):
        return  True
    else:
        return  False

