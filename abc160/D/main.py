from collections import deque

N, X, Y = map(int, input().split())
X -= 1
Y -= 1

dist = [[-1] * N for _ in range(N)]

i = 0
while i < N:
  que = deque()
  que.append(i)
  while len(que) > 0:
    v = que.popleft()
    values = []
    if v > 0:
      values.append(v - 1)
    if v < N - 1:
      values.append(v + 1)
    if v == X:
      values.append(Y)
    if v == Y:
      values.append(X)
    for v2 in values:
      if dist[i][v2] == -1:
        dist[i][v2] = dist[i][v] + 1
        que.append(v2)
  i += 1

res = [0] * N
for i in range(N):
  for j in range(i + 1, N):
    res[dist[i][j]] += 1

for i in range(N - 1):
  print(res[i])


