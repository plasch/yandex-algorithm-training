# C.Частотный анализ

text = open("input.txt", "r").read()
words = {}
for i in text.split():
    words[i] = words.get(i, 0) + 1
    # if i not in words:
    #     words[i] = 1
    # else:
    #     words[i] += 1

# result = [(v, k) for k, v in words.items()]
for i in sorted(words.items(), key=lambda i :(-i[1], i[0])):
    print(i[0])
