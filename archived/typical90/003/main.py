# https://qiita.com/wihan23/items/b6934280491124bc5767
from collections import deque

N = int(input())
graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
  A, B = map(int, input().split())
  graph[A].append(B)
  graph[B].append(A)

def bfs(que, dist):
  while(que):
    city = que.popleft()
    d = dist[city]
    for next_city in graph[city]:
      if dist[next_city] == -1:
        que.append(next_city)
        dist[next_city] = d + 1
  return dist

def get_furthest(start):
  dist = [-1] * (N + 1)
  que = deque()
  que.append(start)
  dist[start] = 0
  dist = bfs(que, dist)
  furthest = max(dist)
  return {'idx': dist.index(furthest), 'val': furthest}

# 1: 都市1から最も遠い都市を探索
furthest_from_1 = get_furthest(1)

# 都市1から最も遠い都市から、最も遠い都市を探索
res = get_furthest(furthest_from_1['idx'])
ans = res['val'] + 1
print(ans)
