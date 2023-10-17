N, S = map(int, input().split())
bags = [tuple(map(int, input().split())) for _ in range(N)]

# do[i][j]: i日目までに合計j円の買い物がが可能かどうか
dp = [[False] * (S + 1) for _ in range(N + 1)]
dp[0][0] = True

for i in range(1, N + 1):
  a, b = bags[i - 1]
  for j in range(S + 1):
    if j - a >= 0 and dp[i - 1][j - a]:
      dp[i][j] = True
    if j - b >= 0 and dp[i - 1][j - b]:
      dp[i][j] = True

if dp[-1][-1] == False:
  print('Impossible')
  exit()

ans = []
current = S
for i in range(N, 0, -1):
  a, b = bags[i - 1]
  if current - a >= 0 and dp[i - 1][current - a]:
    ans.append('A')
    current -= a
  else:
    ans.append('B')
    current -= b

ans = ''.join(reversed(ans))
print(ans)
