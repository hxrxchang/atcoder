# 簡易データで考えるとわかりやすい
# N = 6
# S = "aatctc"
# target_char = "atc"

N = int(input())
S = input()
target_char = "atcoder"

# dp[i][j]: Sのi文字目までの文字列で、文字列 "atcoder" のj文字目までを作れるパターン数
dp = [[0] * len(target_char) for _ in range(N)]

# 前処理: dp[i][0] つまり Sのi文字目までに に 'a' が何文字あるか計算
if S[0] == target_char[0]:
  dp[0][0] = 1
for i in range(1, N):
  if S[i] == target_char[0]:
    dp[i][0] = dp[i - 1][0] + 1
  else:
    dp[i][0] = dp[i - 1][0]

for i in range(1, N):
  for j in range(1, len(target_char)):
    if S[i] == target_char[j]:
      dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    else:
      dp[i][j] = dp[i - 1][j]
    dp[i][j] %= 10 ** 9 + 7

print(dp[-1][-1])
