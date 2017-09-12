import math
import numpy as np

from Classes.Point import Point
from Classes.Polygon import Polygon

class PolygonalCylinder():
    def __init__(self, verticesNumber=8, thickness=1, outerRadius=1):
        centralAngle = 2 * math.pi / verticesNumber
        self.__facets = []
        top = []
        bottom = []
        for i in range(int(verticesNumber)):
            vertices = []
            top.append(Point(outerRadius * math.cos(centralAngle * i),
                             outerRadius * math.sin(centralAngle * i),
                             thickness / 2))
            top.append(Point(outerRadius * math.cos(centralAngle * (i - 1)),
                             outerRadius * math.sin(centralAngle * (i - 1)),
                             thickness / 2))
            bottom.append(Point(outerRadius * math.cos(centralAngle * i),
                                outerRadius * math.sin(centralAngle * i),
                                -thickness / 2))
            bottom.append(Point(outerRadius * math.cos(centralAngle * (i - 1)),
                                outerRadius * math.sin(centralAngle * (i - 1)),
                               -thickness / 2))
            vertices.append(Point(outerRadius * math.cos(centralAngle * i),
                                  outerRadius * math.sin(centralAngle * i),
                                  thickness / 2))
            vertices.append(Point(outerRadius * math.cos(centralAngle * i),
                                  outerRadius * math.sin(centralAngle * i),
                                  -thickness / 2))
            vertices.append(Point(outerRadius * math.cos(centralAngle * (i - 1)),
                                  outerRadius * math.sin(centralAngle * (i - 1)),
                                  thickness / 2))
            vertices.append(Point(outerRadius * math.cos(centralAngle * (i - 1)),
                                  outerRadius * math.sin(centralAngle * (i - 1)),
                                  -thickness / 2))
            self.__facets.append(Polygon(vertices))
        self.__topFacet = Polygon(top)
        self.__bottomFacet = Polygon(bottom)
            
    def facets(self):
        return self.__facets
        
    def topFacet(self):
        return self.__topFacet
        
    def bottomFacet(self):
        return self.__bottomFacet
        
    def ifCrossesOtherPolygonalCylinder(self, otherPc):
        polygons = [self.topFacet(), self.bottomFacet(), *self.facets()]
        otherPolygons = [otherPc.topFacet(), otherPc.bottomFacet(), *otherPc.facets()]
        for i in range(len(polygons)):
            for j in range(len(otherPolygons)):
                if polygons[i].ifCrossesOtherPolygon(otherPolygons[j]):
                    return True
        return False
        
    def translateInX(self, dx):
        self.translate(dx, 0, 0)
    
    def translateInY(self, dy):
        self.translate(0, dy, 0)
    
    def translateInZ(self, dz):
        self.translate(0, 0, dz)
    
    def translate(self, dx, dy, dz):
        M = np.array([
                      [1, 0, 0, 0],
                      [0, 1, 0, 0],
                      [0, 0, 1, 0],
                      [dx, dy, dz, 1]
                     ])
        polygons = [self.topFacet(), self.bottomFacet(), *self.facets()]
        for i in range(len(polygons)):
            pts = []
            for pt in polygons[i].vertices():
                pt = np.array([pt.x(), pt.y(), pt.z(), 1])
                pt = np.dot(pt, M)
                pt = Point(pt[0], pt[1], pt[2])
                pts.append(pt)
            polygons[i] = Polygon(pts)
        self.setTopFacet(polygons[0])
        self.setBottomFacet(polygons[1])
        self.setFacets(polygons[2::])
        
    def rotateAroundX(self, alpha):
        M = np.array([
                      [1, 0, 0, 0],
                      [0, math.cos(alpha), -math.sin(alpha), 0],
                      [0, math.sin(alpha), math.cos(alpha), 0],
                      [0, 0, 0, 1]
                     ])
        polygons = [self.topFacet(), self.bottomFacet(), *self.facets()]
        for i in range(len(polygons)):
            pts = []
            for pt in polygons[i].vertices():
                pt = np.array([pt.x(), pt.y(), pt.z(), 1])
                pt = np.dot(pt, M)
                pt = Point(pt[0], pt[1], pt[2])
                pts.append(pt)
            polygons[i] = Polygon(pts)
        self.setTopFacet(polygons[0])
        self.setBottomFacet(polygons[1])
        self.setFacets(polygons[2::])
    
    def rotateAroundY(self, beta):
        M = np.array([
                      [math.cos(beta), 0, math.sin(beta), 0],
                      [0, 1, 0, 0],
                      [-math.sin(beta), 0, math.cos(beta), 0],
                      [0, 0, 0, 1]
                     ])
        polygons = [self.topFacet(), self.bottomFacet(), *self.facets()]
        for i in range(len(polygons)):
            pts = []
            for pt in polygons[i].vertices():
                pt = np.array([pt.x(), pt.y(), pt.z(), 1])
                pt = np.dot(pt, M)
                pt = Point(pt[0], pt[1], pt[2])
                pts.append(pt)
            polygons[i] = Polygon(pts)
        self.setTopFacet(polygons[0])
        self.setBottomFacet(polygons[1])
        self.setFacets(polygons[2::])
    
    def rotateAroundZ(self, gamma):
        M = np.array([
                      [math.cos(gamma), -math.sin(gamma), 0, 0],
                      [math.sin(gamma), math.cos(gamma), 0, 0],
                      [0, 0, 1, 0],
                      [0, 0, 0, 1]
                     ])
        polygons = [self.topFacet(), self.bottomFacet(), *self.facets()]
        for i in range(len(polygons)):
            pts = []
            for pt in polygons[i].vertices():
                pt = np.array([pt.x(), pt.y(), pt.z(), 1])
                pt = np.dot(pt, M)
                pt = Point(pt[0], pt[1], pt[2])
                pts.append(pt)
            polygons[i] = Polygon(pts)
        self.setTopFacet(polygons[0])
        self.setBottomFacet(polygons[1])
        self.setFacets(polygons[2::])
                
    def setTopFacet(self, topFacet):
        self.__topFacet = topFacet
        
    def setBottomFacet(self, bottomFacet):
        self.__bottomFacet = bottomFacet
        
    def setFacets(self, facets):
        self.__facets = facets