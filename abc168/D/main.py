from collections import deque

N, M = map(int, input().split())
N -= 1
M -= 1
graph = [[] for _ in range(N + 1)]
for _ in range(N):
  A, B = map(int, input().split())
  A -= 1
  B -= 1
  graph[A].append(B)
  graph[B].append(A)

dist = [-1] * N
prev = [-1] * N
que = deque()
que.append(0)
dist[0] = 0
print(graph)
while(len(que) > 0):
  v = que.popleft()
  for nv in graph[v]:
    if dist[nv] == -1:
      dist[nv] = dist[v] + 1
      prev[nv] = v
      que.append(nv)
print("Yes")
for i in range(1, N):
  print(prev[i] + 1)


