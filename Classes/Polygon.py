import numpy as np

from Classes.LineSegment import LineSegment
from Classes.Options import Options
from Classes.Plane import Plane
from Classes.Point import Point
from Classes.Vector import Vector


class Polygon():
    def __init__(self, vertices):
        self.__vertices = vertices
        self.__o = Options()

    def vertices(self):
        return self.__vertices

    def ifCrossesOtherPolygon(self, otherPolygon):
        otherVertices = otherPolygon.vertices()
        vertices = self.__vertices
        otherCenter = Vector(x=0, y=0, z=0)
        center = Vector(x=0, y=0, z=0)
        for pt in otherVertices:
            v = Vector(x=pt.x(), y=pt.y(), z=pt.z())
            otherCenter = otherCenter + v
        otherCenter = otherCenter / (len(otherVertices))
        for pt in vertices:
            v = Vector(x=pt.x(), y=pt.y(), z=pt.z())
            center = center + v
        center = center / (len(otherVertices))
        otherPlane = Plane(pt0=otherVertices[0],
                           pt1=otherVertices[1],
                           pt2=otherVertices[2])
        plane = Plane(pt0=vertices[0],
                      pt1=vertices[1],
                      pt2=vertices[2])
        flagSelfCrossesOther = 0
        flagOtherCrossesSelf = 0
        for i, vertex in enumerate(vertices):
            if i == 0:
                continue
            ls = LineSegment(vertices[0], vertex)
            if otherPlane.ifIsCrossedByLineSegment(ls):
                ptCross = otherPlane.ptCross()
                if otherPolygon.ifContainsPoint(ptCross):
                    flagSelfCrossesOther = 1
                    break
        if flagSelfCrossesOther == 0:
            return False
        for i, otherVertex in enumerate(otherVertices):
            if i == 0:
                continue
            ls = LineSegment(otherVertices[0], otherVertex)
            if plane.ifIsCrossedByLineSegment(ls):
                ptCross = plane.ptCross()
                if self.ifContainsPoint(ptCross):
                    flagOtherCrossesSelf = 1
                    break
        if flagOtherCrossesSelf == 0:
            return False
        return True
        
    def ifContainsPoint(self, pt):
        maxDist = 0
        for vertex in self.vertices():
            maxDist += Vector(begin=self.vertices()[0], end=vertex).l()
        dist = 0
        for vertex in self.vertices():
            dist += Vector(begin=pt, end=vertex).l()
        if dist < maxDist:
            return True
        return False