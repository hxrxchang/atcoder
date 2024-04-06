from collections import deque
import copy

N, M = map(int, input().split())
G = []
walls = []
not_walls = []
for i in range(N):
  m = list(input())
  for j in range(len(m)):
    if m[j] == "#":
      walls.append((i, j))
    else:
      not_walls.append((i, j))
  G.append(m)

cnt = 0
for wall in walls:
  G2 = copy.deepcopy(G)
  G2[wall[0]][wall[1]] = "."
  not_walls_2 = copy.deepcopy(not_walls)
  not_walls_2.append((wall))

  que = deque()
  que.append(not_walls[0])
  dist = [[-1] * M for _ in range(N)]
  dist[not_walls[0][0]][not_walls[0][1]] = 0
  while len(que) > 0:
    item = que.popleft()
    y, x = item[0], item[1]
    d = dist[y][x]
    directions = [
      (y + 1, x), #上
      (y - 1, x), #下
      (y, x + 1), #右
      (y, x - 1)  #左
    ]
    for dir in directions:
      y2, x2 = dir[0], dir[1]
      if 0 <= y2 and y2 < N and 0 <= x2 and x2 < M:
        if G2[y2][x2] == '.' and dist[y2][x2] == -1:
          que.append((y2, x2))
          dist[y2][x2] = d + 1

  flag = True
  for item in not_walls_2:
    y, x = item[0], item[1]
    if dist[y][x] == -1:
      flag = False
      break

  if flag == True:
    cnt += 1

print(cnt)
