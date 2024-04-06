N, M = map(int, input().split())
P = [0]
for p in list(map(int, input().split())):
  P.append(p-1)

# dp[i]: i番目が何世代あとまで保険を賄えるか。0の場合は自分までが保険に入っている。-1の場合は未加入
dp = [-1] * N

for _ in range(M):
  x, y = map(int, input().split())
  dp[x-1] = max(dp[x-1], y)

for i in range(1, N):
  # 自分の親が何世代保険を賄えるかみる。-1するのは自分の分を減らすため。
  dp[i] = max(dp[i], dp[P[i]] - 1)

ans = 0
for d in dp:
  if d >= 0:
    ans += 1

print(ans)
