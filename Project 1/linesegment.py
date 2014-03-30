# CS 241 HW 1
# linesegment.py
#
# Made by: Michelle Chen
#
# Defines a class that represents a line segment on a Cartesian plane.

from point import Point

class LineSegment:

    # The class constructor that initializes a line segment by storing
    # the two end points in the two attributes self.pointA and self.pointB.
    def __init__(self, pointA, pointB):
        self._pointA = pointA
        self._pointB = pointB
    
    # Returns Point A endpoint
    def endPointA(self):
        return self._pointA
    
    # Returns Point B endpoint
    def endPointB(self):
        return self._pointB
    
    # Determines the length of the line segment
    def length(self):
        import math
        return math.sqrt((self._pointA._x - self._pointB._x) ** 2 + (self._pointA._y - self._pointB._y) ** 2)
    
    # Determines if the line segment is vertical or parallel to the x-axis
    # True if vertical, false otherwise
    def isVertical(self):
        return self._pointA._x - self._pointB._x == 0
    
    # Determines if the line segment is horizontal or parallel to the x-axis
    # True if vertical, false otherwise
    def isHorizontal(self):
        return self._pointA._y - self._pointB._y == 0
    
    # Determines if two line segments are parallel
    # True if parallel, false otherwise
    def isParallel(self, otherLine):
        return self.slope() == otherLine.slope()
   
    def isPerpendicular(self, otherLine):
        if (self._pointA._x - self._pointB._x) != 0 and \
           (otherLine._pointA._x - otherLine._pointB._x) != 0:
            slopeOne = ((self._pointA._y - self._pointB._y) / (self._pointA._x - self._pointB._x))
            slopeTwo = ((otherLine._pointA._y - otherLine._pointB._y) / (otherLine._pointA._x - otherLine._pointB._x))
            if slopeTwo or slopeOne != 0:
                return slopeOne == (-1 / slopeTwo) or (-1 / slopeOne) == slopeTwo
            else:
                return False
        else:
            if (self._pointA._x - self._pointB._x) == 0 and \
            (otherLine._pointA._x - otherLine._pointB._x) == 0:
                return False

    # Determines the slope of the line segment
    # Returns false if the line segment is vertical
    def slope(self):
        if (self._pointA._x - self._pointB._x) != 0:
            return (self._pointA._y - self._pointB._y) / (self._pointA._x - self._pointB._x)
        
        else:
            return False
    
    # Determines the midpoint of a line segment
    def midPoint(self):
        return Point((self._pointA._x + self._pointB._x) / 2, (self._pointA._y + self._pointB._y) / 2)
    
    
    def __str__(self):
        a = '(' + str(self._pointA._x) + ", " + str(self._pointA._y) + ')'
        b = '(' + str(self._pointB._x) + ", " + str(self._pointB._y) + ')'
        return a + '#' + b
        


