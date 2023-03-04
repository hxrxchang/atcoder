from collections import deque, Counter
from time import sleep

def dfs(n, comp, G):
  visited = [False] * n
  que = deque()
  for i in range(n):
    if visited[i] == False:
      que.append(i)
      while que:
        vertex = que.pop()
        visited[vertex] = True
        comp[vertex] = i
        for neighbor in G[vertex]:
          if visited[neighbor] == False:
            que.append(neighbor)

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
comp = [0] * N
for _ in range(M):
  u, v = map(int, input().split())
  u -= 1
  v -= 1
  graph[u].append(v)
  graph[v].append(u)

dfs(N, comp, graph)
side_cnt = 0
for i in range(max(comp) + 1):
  item_cnt = comp.count(i)
  que = deque()
  if not i in comp:
    continue
  que.append(comp.index(i))
  visited = [False] * N
  visited[comp.index(i)] = True
  while que:
    item = que.popleft()
    for g in graph[item]:
      if not visited[g]:
        que.append(g)
        side_cnt += 1
        visited[g] = True

print(comp)
if max(comp) + 1 == side_cnt:
  print("Yes")
else:
  print("No")
