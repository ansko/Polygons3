#!/usr/bin/env python3
# coding utf-8

import math
import random

from Classes.LineSegment import LineSegment
from Classes.Options import Options
from Classes.Point import Point
from Classes.Polygon import Polygon
from Classes.PolygonalCylinder import PolygonalCylinder
from Classes.Plane import Plane
from Classes.Vector import Vector


def main():
    o = Options()
    fname = o.getProperty('fname')
    f = open(fname, 'w')
    f.write('algebraic3d\n')
    plc1 = PolygonalCylinder(verticesNumber=o.getProperty('verticesNumber'),
                             thickness=o.getProperty('polygonalDiskThickness'),
                             outerRadius=o.getProperty('polygonalDiskOuterRadius'))
    plc1.translate(random.random(), random.random(), random.random())
    plc1.rotateAroundX(math.pi/2)
    plc1.rotateAroundY(math.pi/4)
    plc1.rotateAroundZ(math.pi/4)
    plc2 = PolygonalCylinder(verticesNumber=o.getProperty('verticesNumber'),
                             thickness=o.getProperty('polygonalDiskThickness'),
                             outerRadius=o.getProperty('polygonalDiskOuterRadius'))
    plc2.translate(-random.random(), -random.random(), -random.random())
    for j, plc in enumerate([plc1, plc2]):
        f.write('solid pc{0} '.format(j))
        topPlane = Plane(pt0=plc.topFacet().vertices()[0], pt1=plc.topFacet().vertices()[1], pt2=plc.topFacet().vertices()[2])
        pt0 = topPlane.pt0()
        n  = topPlane.n()
        f.write('= plane({0}, {1}, {2}; {3}, {4}, {5})'.format(pt0.x(), pt0.y(), pt0.z(),
                                                               -n.x(), -n.y(), -n.z()))
        botPlane = Plane(pt0=plc.bottomFacet().vertices()[0], pt1=plc.bottomFacet().vertices()[1], pt2=plc.bottomFacet().vertices()[2])
        pt0 = botPlane.pt0()
        n = botPlane.n()
        f.write(' and plane({0}, {1}, {2}; {3}, {4}, {5})'.format(pt0.x(), pt0.y(), pt0.z(),
                                                                  n.x(), n.y(), n.z()))
        facets = plc.facets()
        for facet in facets:
            vertices = facet.vertices()
            pt0 = vertices[0]
            pt1 = vertices[1]
            pt2 = vertices[2]
            plane = Plane(pt0=pt0, pt1=pt1, pt2=pt2)
            f.write(' and plane({3}, {4}, {5}; {0}, {1}, {2})'.format(-plane.n().x(), -plane.n().y(), -plane.n().z(), pt0.x(), pt0.y(), pt0.z()))
        f.write(';\ntlo pc{0};'.format(j))
        
    print(plc1.ifCrossesOtherPolygonalCylinder(plc2))
    
    
main()
