# E.Автомобильные номера

m = int(input())
symbols = list()
while m > 0:
    symbols.append(input())
    m -= 1

n = int(input())
numbers = list()
while n > 0:
    numbers.append(input())
    n -= 1

count = [0 for _ in range(len(numbers))]

for i in range(len(numbers)):
    for sym in symbols:
        if set(sym).issubset(set(numbers[i])):
            count[i] = count[i] + 1

for i in range(len(count)):
    if count[i] == max(count):
        print(numbers[i])
