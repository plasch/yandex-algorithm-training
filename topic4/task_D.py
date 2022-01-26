# D.Выборы Государственной Думы

text = open("input.txt", "r")
result = []
sum_voice = int()
for i in text:
    line = i.split()
    name, voices = ' '.join(line[0:len(line)-1]), int(line[-1])
    sum_voice += voices
    result.append([name, voices])

print(sum_voice)
print(sum_voice / 450)

sum_place = int()
for i in result:
    print(i[1] % (sum_voice / 450))
    i.append(i[1] % (sum_voice / 450))
    i[1] = i[1] // (sum_voice / 450)
    sum_place += i[1]
print(sum_place)

# if sum_place < 450:

print(result[0][1] % (sum_voice / 450))

for i in result:
    print(*i)

    # place[i] = place.get(i, 0) + 1
    # if i not in words:
    #     words[i] = 1
    # else:
    #     words[i] += 1

# result = [(v, k) for k, v in words.items()]
# for i in sorted(words.items(), key=lambda i :(-i[1], i[0])):
#     print(i[0])

