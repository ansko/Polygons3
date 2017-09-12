import numpy as np

from Classes.LineSegment import LineSegment
from Classes.Point import Point
from Classes.Vector import Vector

class Plane():
    def __init__(self, 
                 a=None, b=None, c=None, d=None,
                 n=None, pt=None,
                 pt0=None, pt1=None, pt2=None):
        self.__pt0 = None
        self.__pt1 = None
        self.__pt2 = None
        self.__ptCross = None
        if ((a is None or b is None or c is None or d is None) and
            (n is None or pt is None) and 
            (pt1 is None or pt2 is None or pt0 is None)):
            print('Cannot define plane!')
            self.__a = None
            self.__b = None
            self.__c = None
            self.__d = None
        elif a is not None and b is not None and c is not None and d is not None:
            self.__a = a
            self.__b = b
            self.__c = c
            self.__d = d
        elif n is not None and pt is not None:
            self.__pt0 = pt
            self.__a = n.x()
            self.__b = n.y()
            self.__c = n.z()
            self.__d = -n.x() * pt.x() - n.y() * pt.y() - n.z() * pt.z()
        elif pt1 is not None and pt2 is not None and pt0 is not None:
            self.__pt0 = pt0
            self.__pt1 = pt1
            self.__pt2 = pt2
            self.__a = (pt1.y() - pt0.y()) * (pt2.z() - pt0.z())
            self.__a -= (pt1.z() - pt0.z()) * (pt2.y() - pt0.y())
            self.__b = -(pt1.x() - pt0.x()) * (pt2.z() - pt0.z())
            self.__b += (pt2.x() - pt0.x()) * (pt1.z() - pt0.z())
            self.__c = (pt1.x() - pt0.x()) * (pt2.y() - pt0.y())
            self.__c -= (pt2.x() - pt0.x()) * (pt1.y() - pt0.y())
            self.__d = -pt0.x() * (pt1.y() - pt0.y()) * (pt2.z() - pt0.z())
            self.__d += pt0.x() * (pt1.z() - pt0.z()) * (pt2.y() - pt0.y())
            self.__d += pt0.y() * (pt1.x() - pt0.x()) * (pt2.z() - pt0.z())
            self.__d -= pt0.y() * (pt2.x() - pt0.x()) * (pt1.z() - pt0.z())
            self.__d -= pt0.z() * (pt1.x() - pt0.x()) * (pt2.y() - pt0.y())
            self.__d += pt0.z() * (pt2.x() - pt0.x()) * (pt1.y() - pt0.y())

    def a(self):
        return self.__a

    def b(self):
        return self.__b

    def c(self):
        return self.__c

    def d(self):
        return self.__d
        
    def n(self):
        return Vector(x=self.a(), y=self.b(), z=self.c())
        
    def pt0(self):
        return self.__pt0

    def inventThreePoints(self):
        if (self.__pt0 is not None and
            self.__pt1 is not None and
            self.__pt2 is not None):
            pass
        elif self.__pt0 is not None and self.__pt1 is not None:
            n = Vector(self.a(), self.b(), self.c())
            v = Vector(self.__pt0, self.__pt1).dot(n)
            self.__pt2 = Point(self.__pt0.x() + v.x(),
                               self.__pt0.y() + v.y(),
                               self.__pt0.z() + v.z())
            pass
        elif self.__pt0 is not None:
            print('Cannot invent points!')
            pass
        else:
            print('Cannot invent points!')
            pass

    def ifIsCrossedByLineSegment(self, ls):
        if (self.__pt0 is not None and
            self.__pt1 is not None and
            self.__pt2 is not None):
            pass
        else:
            print('Should invent points!');
        pt0 = self.__pt0
        pt1 = self.__pt1
        pt2 = self.__pt2
        pt3 = ls.begin()
        pt4 = ls.end()
        v01 = Vector(begin=pt0, end=pt1)
        v02 = Vector(begin=pt0, end=pt2)
        v03 = Vector(begin=pt0, end=pt3)
        v04 = Vector(begin=pt0, end=pt4)
        expressionOne = np.array([
                                  [v01.x(), v01.y(), v01.z()],
                                  [v02.x(), v02.y(), v02.z()],
                                  [v03.x(), v03.y(), v03.z()]
                                 ])
        expressionTwo = np.array([
                                  [v01.x(), v01.y(), v01.z()],
                                  [v02.x(), v02.y(), v02.z()],
                                  [v04.x(), v04.y(), v04.z()]
                                 ])
        det1 = np.linalg.det(expressionOne)
        det2 = np.linalg.det(expressionTwo)
        if det1 * det2 < 0:
            v3 = Vector(pt3.x(), pt3.y(), pt3.z())
            v34 = Vector(begin=pt3, end=pt4)
            vCross = v3 + v34 * abs(det1) / (abs(det1) + abs(det2))
            self.__ptCross = Point(vCross.x(), vCross.y(), vCross.z())
            return True
        elif det1 == 0:
            self.__ptCross = pt3
            return True
        elif det2 == 0:
            self.__ptCross = pt4
            return True
        return False

    def ptCross(self):
        return self.__ptCross