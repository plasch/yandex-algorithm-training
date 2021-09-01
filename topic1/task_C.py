# C.Даты

x, y, z = map(int, input().split())

if 12 < x <= 31 and y <= 12:
    print(1)
elif x <= 12 and 12 < y <= 31:
    print(1)
elif x == y:
    print(1)
else:
    print(0)
