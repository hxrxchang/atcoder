INF = float('inf')

H, N = map(int, input().split())
magics = [tuple(map(int, input().split())) for _ in range(N)]

# dp[i][j]: i番目までの魔法を使って(何回使ってもいい)モンスターの体力をj以上消費するにするのに必要な最小のコスト
dp = [[INF] * (H + 1) for _ in range(N + 1)]
dp[0][0] = 0

for i in range(N):
  for j in range(H + 1):
    a, b = magics[i]
    dp[i + 1][j] = min(dp[i][j], dp[i + 1][max(0, j - a)] + b) # max(0, j - a)はj - aが負の場合に対応するため

print(dp[N][H])
