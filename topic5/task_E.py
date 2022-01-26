# E.Сумма трёх

s = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

Am, Bm, Cm = A[1:], B[1:], C[1:]

ans = [-1]
for i in range(A[0]):
    for j in range(B[0]):
        for k in range(C[0]):
            if Am[i] + Bm[j] + Cm[k] == s:
                ans.append([i, j, k])

if len(ans) != 1:
    print(*min(ans[1:]))
else:
    print(*ans)
