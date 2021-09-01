# D.Строительство школы

N = int(input())
houses_list = [int(x) for x in input().split()]

n = int(N / 2 + 1)
print(houses_list[n - 1])
