from heapq import heappop, heappush

INF = 1 << 63

N, M = map(int, input().split())
G_rev = [[] for _ in range(N)]
for _ in range(M):
    l, d, k, c, A, B = map(int, input().split())
    A, B = A - 1, B - 1
    G_rev[B].append((l, d, k, c, A))

dp = [-INF] * N
dp[-1] = INF

que = []
heappush(que, (-INF, N - 1))  # (-last_time, station)
while que:
    mt, station = heappop(que)
    pt = -mt
    if dp[station] != pt:
        continue
    for l, d, k, c, A in G_rev[station]:
        x = min((pt - l - c) // d, k - 1)
        if x < 0:
            continue
        nt = l + x * d
        if dp[A] < nt:
            dp[A] = nt
            heappush(que, (-nt, A))

for i in range(N - 1):
    print(dp[i] if dp[i] != -INF else 'Unreachable')
