HOLES_LEN = 5
N = int(input())

snukes =[]
max_T = 0
for _ in range(N):
    T, X, A = map(int, input().split())
    snukes.append([T, X, A])
    max_T = max(max_T, T)

# snukes[i][j]: i経過後にjにいるときのスヌケの大きさ
snukes2 = [[0] * HOLES_LEN for _ in range(max_T + 1)]
for T, X, A in snukes:
    snukes2[T][X] = A

dp = snukes2[0]

for time in range(1, max_T + 1):
    tmp = dp[:]
    for hole in range(HOLES_LEN):
        dp[hole] = max(tmp[max(0, hole - 1)], tmp[hole], tmp[min(HOLES_LEN - 1, hole + 1)])
        if time >= hole:
            dp[hole] += snukes2[time][hole]

print(max(dp))


