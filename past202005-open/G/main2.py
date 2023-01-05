from collections import deque

N, X, Y = map(int, input().split())
stops = []
for _ in range(N):
  x, y = map(int, input().split())
  stops.append((x, y))

que = deque()
que.append((0, 0))
dist = {"0,0": 0}

while len(que) > 0:
  queitem = que.popleft()
  x, y = queitem[0], queitem[1]
  if x == X and y == Y:
    break
  d = dist[str(x) + ',' + str(y)]
  items = [(x + 1, y + 1), (x, y + 1), (x - 1, y + 1), (x + 1, y), (x - 1, y), (x, y -1 )]
  for item in items:
    x2, y2 = item[0], item[1]
    if -250 <= x2 and x2 <= 250 and -250 <= y2 and y2 <= 250:
      if not str(x2) + ',' + str(y2) in dist and not (x2, y2) in stops:
        dist[str(x2) + ',' + str(y2)] = d + 1
        que.append((x2, y2))

if not str(x) + ',' + str(y) in dist:
  print(-1)
else:
  print(dist[str(x) + ',' + str(y)])
