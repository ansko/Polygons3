from Classes.Point import Point


class Vector(Point):
    def __init__(self, x=None, y=None, z=None, begin=None, end=None):
        if ((x is None or y is None or z is None) and
            (begin is None or end is None)):
            self.__x = 0
            self.__y = 0
            self.__z = 0
        elif begin is not None and end is not None:
            self.__x = end.x() - begin.x()
            self.__y = end.y() - begin.y()
            self.__z = end.z() - begin.z()
            #print(self.x(), self.y(), self.z())
        elif x is not None and y is not None and z is not None:
            self.__x = x
            self.__y = y
            self.__z = z

    def __add__(self, otherVector):
        x = self.__x + otherVector.x()
        y = self.__y + otherVector.y()
        z = self.__z + otherVector.z()
        return Vector(x, y, z)

    def __sub__(self, otherVector):
        x = self.__x - otherVector.x()
        y = self.__y - otherVector.y()
        z = self.__z - otherVector.z()
        return Vector(x, y, z)

    def __mul__(self, coefficient):
        x = self.__x * coefficient
        y = self.__y * coefficient
        z = self.__z * coefficient
        return Vector(x, y, z)
        
    def __rmul__(self, coefficient):
        x = self.__x * coefficient
        y = self.__y * coefficient
        z = self.__z * coefficient
        return Vector(x, y, z)

    def __truediv__(self, coefficient):
        if coefficient == 0:
            print('You want divide by 0!')
            return None
        x = self.__x / coefficient
        y = self.__y / coefficient
        z = self.__z / coefficient
        return Vector(x, y, z)

    def x(self):
        return self.__x

    def y(self):
        return self.__y

    def z(self):
        return self.__z

    def dot(self, otherVector):
        x = self.y() * otherVector.z() - self.z() * otherVector.y() 
        y = self.z() * otherVector.x() - self.x() * otherVector.z()
        z = self.x() * otherVector.y() - self.y() * otherVector.x()
        return Vector(x, y, z)

    def scalarMultiply(self, otherVector):
        return (self.x() * otherVector.x() +
                self.y() * otherVector.y() +
                self.z() * otherVector.z())

    def l(self):
        return (self.x()**2 + self.y()**2 + self.z()**2)**0.5
