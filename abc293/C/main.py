import sys
sys.setrecursionlimit(10 ** 6)
from collections import deque

H, W = map(int, input().split())
graph = []
for _ in range(H):
  row = list(map(int, input().split()))
  graph.append(row)

dist = [[None] * W for _ in range(H)]
dist[0][0] = 0

que = deque()
que.append((0, 0))
tmp = set()
tmp.add(graph[0][0])
cnt = 0
while len(que):
  y, x = que.popleft()
  for y2, x2 in [(y + 1, x), (y, x + 1)]:
    if y2 < H and x2 < W:
      if not graph[y2][x2] in tmp:
        tmp.add(graph[y2][x2])
        que.append((y2, x2))
  if y == H - 1 and x == W - 1:
    cnt += 1

print(cnt)
