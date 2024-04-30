N, W = map(int, input().split())
items = []
total_v = 0
for _ in range(N):
    w, v = map(int, input().split())
    items.append((w, v))
    total_v += v

dp = [float('inf')] * (total_v + 1)
dp[0] = 0

for w, v in items:
    tmp = dp[:]
    for v2 in range(1, total_v + 1):
        if v2 - v >= 0:
            tmp[v2] = min(dp[v2], dp[v2 - v] + w)
    dp = tmp

ans = 0
for i, weight in enumerate(dp):
    if weight <= W:
        ans = i

print(ans)


