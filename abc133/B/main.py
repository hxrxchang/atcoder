import math

N, D = map(int, input().split())

nodes = [list(map(int, input().split())) for _ in range(N)]

cnt = 0

for i in range(N):
    for j in range(i + 1, N):
        y = nodes[i]
        z = nodes[j]
        tmp = 0
        for k in range(D):
            tmp += (y[k] - z[k]) ** 2
        if math.sqrt(tmp) % 1 == 0:
            cnt += 1

print(cnt)
