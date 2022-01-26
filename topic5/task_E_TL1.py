# E.Сумма трёх
from itertools import product

s = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

Am, Bm, Cm = A[1:], B[1:], C[1:]

ans = [-1]
for i, j, k in product(range(A[0]), range(B[0]), range(C[0])):
    if Am[i] + Bm[j] + Cm[k] == s:
        ans.append([i, j, k])

if len(ans) != 1:
    print(*min(ans[1:]))
else:
    print(*ans)
