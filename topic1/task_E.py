# E.Точка и треугольник

d = int(input())
x0, y0 = map(int, input().split())

x1, y1 = 0, 0
x2, y2 = d, 0
x3, y3 = 0, d

p1 = (x1-x0)*(y2-y1)-(x2-x1)*(y1-y0)
p2 = (x2-x0)*(y3-y2)-(x3-x2)*(y2-y0)
p3 = (x3-x0)*(y1-y3)-(x1-x3)*(y3-y0)

l1 = ((x1-x0)**2 + (y1-y0)**2)**0.5
l2 = ((x2-x0)**2 + (y2-y0)**2)**0.5
l3 = ((x3-x0)**2 + (y3-y0)**2)**0.5

minimal = min(l1, l2, l3)

if (p1 > 0 and p2 > 0 and p3 > 0) or (p1 < 0 and p2 < 0 and p3 < 0):
    print(0)    # если они одинакового знака, то точка внутри треугольника
elif p1 == 0 or p2 == 0 or p2 == 0:
    print(0)    # если что-то из этого - ноль, то точка лежит на стороне
# точка вне треугольника
else:
    if minimal == l1:
        print(1)
    elif minimal == l2:
        print(2)
    else:
        print(3)
