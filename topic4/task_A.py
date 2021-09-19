# A.Толя-Карп и новый набор структур, часть 2

n = int(input())
result = {}
while n > 0:
    d, a = map(int, input().split())
    if d not in result:
        result[d] = a
    else:
        result[d] += a
    n -= 1

for i in sorted(result):
    print(i, result[i])
