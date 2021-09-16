# D.Угадай число

n = int(input())
vvod = input()

answer_no = []
answer_yes = [str(i) for i in range(1, n + 1)]
answer = vvod

while vvod != "HELP":
    if vvod == "YES":
        if not answer_yes:
            answer_yes += answer.split()
        else:
            answer_yes = set(answer_yes).intersection(set(answer.split()))
    elif vvod == "NO":
        answer_no += answer.split()
    else:
        answer = vvod
    vvod = input()

print(' '.join((sorted(list(set(answer_yes) - set(answer_no))))))
