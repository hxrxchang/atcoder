N, M = map(int, input().split())

dp = [0] * (N + 1)
# 0から1に行く方法は1通り
dp[0] = 1
dp[1] = 1
for _ in range(M):
  stair = int(input())
  dp[stair] = -1

for n in range(2, N + 1):
  if dp[n] == -1:
    continue

  a, b = dp[n - 1], dp[n - 2]
  # 1段前と2段前が壊れている場合はその時点で移動不可能
  if a == -1 and b == -1:
    break

  if a == -1:
    dp[n] = b
  elif b == -1:
    dp[n] = a
  else:
    dp[n] = a + b

ans = dp[-1] % 1000000007
print(ans)





