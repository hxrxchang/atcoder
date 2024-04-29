N, W = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(N)]

dp = [-1] * (W + 1)
dp[0] = 0

for w, v in items:
    tmp = dp[:]
    for weight in range(1, W + 1):
        if w <= weight:
            tmp[weight] = max(dp[weight], dp[weight - w] + v)
    dp = tmp

print(max(dp))
