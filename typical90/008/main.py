N = int(input())
S = input()
atcoder = "atcoder"
division_number = 10 ** 9 + 7

# dp[i][j]: Sのi文字目までを用いた時、文字列"atcoder"のj文字目までを作る通りの数
dp = []
for _ in range(N + 1):
  row = [0] * (len(atcoder) + 1)
  dp.append(row)

# j=0 つまり文字を取り出さない方法は1通りのため
for i in range(N + 1):
  dp[i][0] = 1

for i in range(N):
  for j in range(len(atcoder)):
    if S[i] == atcoder[j]:
      dp[i + 1][j + 1] = (dp[i][j] + dp[i][j + 1]) % division_number
    else:
      dp[i + 1][j + 1] = dp[i][j + 1]

print(dp[N][len(atcoder)])

# # ↓で確認するとわかりやすい
# for i in range(len(dp)):
#   print(S[i - 1], dp[i])

