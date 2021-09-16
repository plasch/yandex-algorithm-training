# A.Количество совпадающих

list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
print(len(set(list1).intersection(set(list2))))
