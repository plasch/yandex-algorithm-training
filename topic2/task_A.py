# A.Количество равных максимальному

max = 0
max_count = 0
n = int(input())
while n != 0:
    if n > max:
        max = n
        max_count = 0
    if n == max:
        max_count += 1
    n = int(input())
print(max_count)
