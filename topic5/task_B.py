# B.Максимальная сумма

n = int(input())
nums = list(map(int, input().split()))

prefixsum = [0] * (n + 1)
for i in range(1, n + 1):
    prefixsum[i] = prefixsum[i - 1] + nums[i - 1]

print(prefixsum)
print(max(prefixsum[1:n+1]))
