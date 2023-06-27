INF = float('inf')

H, N = map(int, input().split())
magics = [tuple(map(int, input().split())) for _ in range(N)]

# dp[i][j]: i番目までの魔法を使ってモンスターの体力をjにするのに必要な最小のコスト
dp = [[INF] * (H + 1) for _ in range(N + 1)]
dp[0][0] = 0

for i in range(N):
  for j in range(H + 1):
    dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])
    a, b = magics[i][0], magics[i][1]
    dp[i + 1][min(j + a, H)] = min(dp[i + 1][min(j + a, H)], dp[i + 1][j] + b)

print(dp[N][H])
