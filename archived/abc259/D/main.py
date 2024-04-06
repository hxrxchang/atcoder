from collections import deque

N = int(input())
Sx, Sy, Tx, Ty = map(int, input().split())

start = None

circles = []
for i in range(N):
  x, y, r = map(int, input().split())
  circles.append((x, y, r))
  if start == None:
    if (x - Sx) ** 2 + (y - Sy) ** 2 == r ** 2:
      start = i

if start == None:
  print('No')
  exit()

que = deque([start])
not_visited_circles = set(range(N))
not_visited_circles.remove(start)

while que:
  circle = circles[que.popleft()]
  x, y, r = circle[0], circle[1], circle[2]
  if (x - Tx) ** 2 + (y - Ty) ** 2 == r ** 2:
    print('Yes')
    exit()

  for i in list(not_visited_circles):
    x2, y2, r2 = circles[i][0], circles[i][1], circles[i][2]
    if (x - x2) ** 2 + (y - y2) ** 2 > (r + r2) ** 2 or (x - x2) ** 2 + (y - y2) ** 2 < (r - r2) ** 2:
      continue
    else:
      que.append(i)
      not_visited_circles.remove(i)

print('No')
