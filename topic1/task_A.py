# A.Interactor

r = int(input())
i = int(input())
c = int(input())
system_verdict = int()

if i == 0:
    if r != 0:
        system_verdict = 3
    else:
        system_verdict = c
elif i == 1:
    system_verdict = c
elif i == 4:
    if r != 0:
        system_verdict = 3
    else:
        system_verdict = 4
elif i == 6:
    system_verdict = 0
elif i == 7:
    system_verdict = 1
else:
    system_verdict = i

print(system_verdict)
