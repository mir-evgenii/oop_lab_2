from point3d import point3d

p3d1 = point3d(1.0, 2.0, 3.0)
p3d2 = point3d(2.0, 2.5, 5.0)
p3d3 = point3d(3.0, 4.5, 6.0)

a = p3d1.distanse_to(p3d2)
b = p3d2.distanse_to(p3d3)
c = p3d3.distanse_to(p3d1)

res = point3d.compute_area(a, b, c)

print('Площадь треугольника = ' + str(res))

