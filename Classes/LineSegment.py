from Classes.Point import Point


class LineSegment():
    def __init__(self, ptBegin, ptEnd):
        self.__begin = ptBegin
        self.__end = ptEnd

    def x(self):
        return self.__end.x() - self.__begin.x()

    def y(self):
        return self.__end.y() - self.__begin.y()

    def z(self):
        return self.__end.z() - self.__begin.z()

    def l(self):
        return (self.x()**2 + self.y()**2 + self.z()**2)**0.5

    def begin(self):
        return self.__begin

    def end(self):
        return self.__end
