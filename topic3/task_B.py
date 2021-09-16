# B.Встречалось ли число раньше

nums = list(map(int, input().split()))

dupl = set()
for i in nums:
    if i in dupl:
        print("YES")
    else:
        print("NO")
    dupl.add(i)
