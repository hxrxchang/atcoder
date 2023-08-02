# 方針: -200 <= x, y, <= 200 を、余裕を持たせて0~500で考える
from collections import deque
MAX = 500
BASE = 250
N, X, Y = map(int, input().split())
X += BASE
Y += BASE
stops = []
for _ in range(N):
  x, y = map(int, input().split())
  x += BASE
  y += BASE
  stops.append((x, y))

que = deque()
que.append((BASE, BASE))
dist = [[-1] * 500 for _ in range(MAX)]
dist[BASE][BASE] = 0

while len(que) > 0:
  queitem = que.popleft()
  x, y = queitem[0], queitem[1]
  if x == X and y == Y:
    break
  d = dist[x][y]
  items = [(x + 1, y + 1), (x, y + 1), (x - 1, y + 1), (x + 1, y), (x - 1, y), (x, y -1 )]
  for item in items:
    x2, y2 = item[0], item[1]
    if 0 <= x2 and x2 < MAX and 0 <= y2 and y2 < MAX:
      if dist[x2][y2] == -1 and not (x2, y2) in stops:
        dist[x2][y2] = d + 1
        que.append((x2, y2))

ans = dist[X][Y]
print(ans)
