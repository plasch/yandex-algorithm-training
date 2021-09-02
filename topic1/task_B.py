# B.Кольцевая линия метро

N, i, j = map(int, input().split())

way1 = int()
way2 = int()

if j > i:
    way1 = (j - i) - 1
    way2 = i + (N - j) - 1
elif j < i:
    way1 = (N - i) + j - 1
    way2 = i - j - 1

if way1 < way2:
    print(way1)
else:
    print(way2)
