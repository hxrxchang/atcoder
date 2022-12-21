from collections import deque

N, X, Y = map(int, input().split())

graph = {i: set() for i in range(1, N + 1)}
for i in range(1, N):
  j = i + 1
  graph[i].add(j)
  graph[j].add(i)
graph[X].add(Y)
graph[Y].add(X)

dist = [[None] * (N + 1) for _ in range(N + 1)]
counter = {i: 0 for i in range(1, N)}
for i in range(1, N + 1):
  que = deque()
  que.append(i)
  dist[i][i] = 0
  while len(que) > 0:
    v = que.popleft()
    for v2 in graph[v]:
      if dist[i][v2] == None:
        cnt = dist[i][v] + 1
        dist[i][v2] = cnt
        counter[cnt] += 1
        que.append(v2)

for i in range(1, N):
  print(counter[i] // 2)
