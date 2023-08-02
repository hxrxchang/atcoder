def judge(a, b):
    if a == b:
        return 0
    elif a == 'G':
        if b == 'C':
            return 1
        else:
            return -1
    elif a == 'C':
        if b == 'P':
            return 1
        else:
            return -1
    else:
        if b == 'G':
            return 1
        else:
            return -1

N, M = map(int, input().split())
A = [list(input()) for _ in range(N * 2)]
ranking = [[i, 0] for i in range(N * 2)]

for i in range(M):
    for j in range(0, N * 2, 2):
        a, b = ranking[j][0], ranking[j + 1][0]
        jud = judge(A[a][i], A[b][i])
        if jud == 0:
            continue
        elif jud == 1:
            ranking[j][1] += 1
        else:
            ranking[j + 1][1] += 1
    ranking.sort(key=lambda x: (-x[1], x[0]))

for r in ranking:
    print(r[0] + 1)
