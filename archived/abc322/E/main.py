N, K, P = map(int, input().split())

tasks = [list(map(int, input().split())) for _ in range(N)]

ans = float('inf')
for i in range(2 ** N):
  parameters = [0] * K
  cost = 0
  for j in range(N):
    if (i >> j) & 1:
      t = tasks[j]
      cost += t[0]
      for k in range(1, K + 1):
        a = t[k]
        parameters[k - 1] += a
  if min(parameters) >= P:
    ans = min(ans, cost)

if ans != float('inf'):
  print(ans)
else:
  print(-1)

