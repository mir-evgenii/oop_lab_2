import math

class point3d:

    def __init__(self, x = 0.0, y = 0.0, z = 0.0):

        self.x = x
        self.y = y
        self.z = z

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_z(self):
        return self.z

    def set_x(self, x = 0.0):
        self.x = x

    def set_y(self, y = 0.0):
        self.y = y

    def set_z(self, z = 0.0):
        self.z = z

    def distanse_to(self, Point3d):

        x = (self.x - Point3d.get_x()) ** 2
        y = (self.y - Point3d.get_y()) ** 2
        z = (self.z - Point3d.get_z()) ** 2

        dist = math.sqrt(x + y + z)

        return dist

    def geron(self, a, b, c):

        p = (a+b+c)/2
        s = (p*(p-a)*(p-b)*(p-c))**0.5
        return s


