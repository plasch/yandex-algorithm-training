# B.Выборы в США

file = open("input.txt", "r")
candidates = dict()
while True:
    # line = input()
    line = file.readline()
    if not line:
        break
    k, v = line.split()
    if k not in candidates:
        candidates[k] = int(v)
    else:
        candidates[k] += int(v)

for i in sorted(candidates):
    print(i, candidates[i])
