# B.Дома и магазины

n = list(map(int, input().split()))

left = [0] * len(n)
shoppos = -20
for i in range(len(n)):
    if n[i] == 2:
        shoppos = i
    if n[i] == 1:
        left[i] = i - shoppos
ans = 0
shoppos = 30
for i in range(len(n) - 1, -1, -1):
    if n[i] == 2:
        shoppos = i
    if n[i] == 1:
        mindist = min(shoppos - i, left[i])
        ans = max(ans, mindist)
print(ans)
