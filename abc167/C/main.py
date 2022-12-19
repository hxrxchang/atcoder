N, M, X = map(int, input().split())

data = []
for _ in range(N):
  data.append(list(map(int, input().split())))

amount_list = []
for i in range(2 ** N):
  amount = 0
  skill = [0] * M
  for j in range(N):
    if ((i >> j) & 1):
      amount += data[j][0]
      for k in range(1, M + 1):
        skill[k - 1] += data[j][k]
  if min(skill) >= X:
    amount_list.append(amount)

if len(amount_list) == 0:
  ans = -1
else:
  ans = min(amount_list)

print(ans)

