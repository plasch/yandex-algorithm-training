# C.Уникальные элементы

nums = list(map(int, input().split()))

for i in nums:
    if nums.count(i) == 1:
        print(i, end=' ')
