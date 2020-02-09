from point2d import point2d
import math

class point3d(point2d):

    def __init__(self, x = 0.0, y = 0.0, z = 0.0):

        point2d.__init__(self, x, y)

        self._z = z

    def get_z(self):
        return self._z

    def set_z(self, z = 0.0):
        self.z = z

    def distanse_to(self, Point3d):

        x = (self._x - Point3d.get_x()) ** 2
        y = (self._y - Point3d.get_y()) ** 2
        z = (self._z - Point3d.get_z()) ** 2

        dist = math.sqrt(x + y + z)

        return dist

    @staticmethod
    def compute_area(a, b, c):

        p = (a+b+c)/2
        s = (p*(p-a)*(p-b)*(p-c))**0.5
        return s

