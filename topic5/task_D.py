# D.Правильная, круглая, скобочная

s = input()
k = 0
for b in s:
    # k += [-1, 1][b == '(']
    if b == '(':
        k += 1
    elif b == ')':
        k -= 1
    if k < 0:
        break
print(['NO', 'YES'][k == 0])
