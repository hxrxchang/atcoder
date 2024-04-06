N, K = map(int, input().split())

limit = 5001

# accum[i][j]: 身長i以下、体重j以下の生徒が何人いるか？
accum = [[0] * limit for _ in range(limit)]

for _ in range(N):
    A, B = map(int, input().split())
    accum[A][B] += 1

for i in range(1, limit):
    for j in range(limit):
        accum[i][j] += accum[i - 1][j]

for i in range(limit):
    for j in range(1, limit):
        accum[i][j] += accum[i][j - 1]

def count(i, j):
    i2 = min(limit - 1, i + K + 1)
    j2 = min(limit - 1, j + K + 1)
    return accum[i][j] + accum[i2][j2] - accum[i][j2] - accum[i2][j]

ans = 0
for i in range(limit):
    for j in range(limit):
        ans = max(ans, count(i, j))

print(ans)
