N, X = map(int, input().split())
moneys = []
money_types = []
for _ in range(N):
  A, B = map(int, input().split())
  moneys.append((A, B))
  money_types.append(A)

dp = []
for _ in range(X + 1):
  row = [0] * (N + 1)
  dp.append(row)
