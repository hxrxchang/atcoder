from collections import deque

N = int(input())

graph = [[] for _ in range(N)]

for _ in range(N - 1):
  u, v = map(int, input().split())
  u, v = u - 1, v - 1
  graph[u].append(v)
  graph[v].append(u)

# 末端のノード(隣接するノードが1つしかないノード)を探す
# それに隣接するノードが星の中心になる
start_node = None
for i in range(N):
  if len(graph[i]) == 1:
    start_node = graph[i][0]
    break

# 星の中心からbfs
dist = [-1] * N
dist[start_node] = 0
que = deque()
que.append(start_node)
while que:
  v = que.popleft()
  for next_node in graph[v]:
    if dist[next_node] == -1:
      dist[next_node] = dist[v] + 1
      que.append(next_node)

ans = []
# スタートノードからの距離が3の倍数のノードが星の中心になる
for i in range(N):
  if dist[i] % 3 == 0:
    ans.append(len(graph[i]))
ans.sort()

print(*ans)
