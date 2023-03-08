from heapq import heappush, heappop

N, M = map(int, input().split())
roads = [[] for _ in range(N)]

for _ in range(M):
  A, B, C = map(int, input().split())
  A -= 1
  B -= 1
  roads[A].append((B, C))
  roads[B].append((A, C))

INF = 2 ** 60

def dijkstra(start, n, edge):
  dist = [INF] * n
  hq = [(0, start)]
  dist[start] = 0
  seen = [False] * N
  while hq:
    v = heappop(hq)[1]
    seen[v] = True
    for to, cost in edge[v]:
      if seen[to] == False and dist[v] + cost < dist[to]:
        dist[to] = dist[v] + cost
        heappush(hq, (dist[to], to))
  return dist

from_start = dijkstra(0, N, roads)
from_end = dijkstra(N - 1, N, roads)

for k in range(N):
  ans = from_start[k] + from_end[k]
  print(ans)
