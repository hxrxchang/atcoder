N = int(input())
S = input()
atcoder = "atcoder"



# dp[i][j] 文字列Sの最初のi文字から何文字か抜き出してつなげて、"atcoder"のj文字目までを作れる数
# S="aatctc" だとしたら、dp[4][1]は "aatct" から "at" を作るパターンは何通りあるか？ということ (=4)
dp = [[0] * len(atcoder) for _ in range(N)]

# dp[i][0] つまり a が何種類あるかを先に計算
for i in range(N):
  if S[i] == atcoder[0]:
    if i - 1 < 0:
      dp[i][0] = 1
    else:
      dp[i][0] = dp[i - 1][0] + 1
  else:
    if i - 1 < 0:
      dp[i][0] = 0
    else:
      dp[i][0] = dp[i - 1][0]

for i in range(1, N):
  for j in range(1, len(atcoder)):
    if S[i] == atcoder[j]:
      dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    else:
      dp[i][j] = dp[i - 1][j]
    dp[i][j] %= 10 ** 9 + 7

print(dp[-1][-1])
