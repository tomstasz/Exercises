import math


def cat_and_mouse(x, y, z):
    if math.fabs(z - x) == math.fabs(z - y):
        return  "Mouse C"
    if math.fabs(z - x) < math.fabs(z - y):
        return "Cat A"
    elif math.fabs(z - x) > math.fabs(z - y):
        return "Cat B"


x = 1
y = 2
z = 3

x1 = 1
y2 = 3
z2 = 2

print(cat_and_mouse(x1, y2, z2))
