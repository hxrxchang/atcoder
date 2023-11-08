from collections import deque

N, M, Q = map(int, input().split())

graph = [[] for _ in range(N)]

for _ in range(M):
  x, y = map(int, input().split())
  x, y = x - 1, y - 1
  graph[x].append(y)

for _ in range(Q):
  A, B = map(int, input().split())
  A, B = A - 1, B - 1
  flag = False
  que = deque()
  que.append(A)
  visited = [False] * N
  while que:
    item = que.popleft()
    if visited[item]:
      continue
    visited[item] = True
    for i in graph[item]:
      if i == B:
        flag = True
        break
      que.append(i)
  if flag:
    print("Yes")
  else:
    print("No")

