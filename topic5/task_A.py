# A.Префиксные суммы

n, q = map(int, input().split())
nums = list(map(int, input().split()))

prefixsum = [0] * (n + 1)
for i in range(1, n + 1):
    prefixsum[i] = prefixsum[i - 1] + nums[i - 1]

ans = list()
while q > 0:
    l, r = map(int, input().split())
    ans.append(str(prefixsum[r] - prefixsum[l - 1]))
    q -= 1
print('\n'.join(ans))
