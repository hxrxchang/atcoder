from collections import deque
inf = 2 ** 60

H, W = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
sy, sx, gy, gx = sy - 1, sx - 1, gy - 1, gx - 1

grid = [list(input()) for _ in range(H)]

dist = [[[inf] * 4] * W for _ in range(H)]

def can_go(y, x):
  return 0 <= y < H and 0 <= x < W and grid[y][x] == '.'

def next_positions(y, x):
  return [(y - 1, x, 0), (y + 1, x, 1), (y, x - 1, 2), (y, x + 1, 3)]

que = deque()

dist[sy][sx][0] = 0
dist[sy][sx][1] = 0
dist[sy][sx][2] = 0
dist[sy][sx][3] = 0

for next in next_positions(sy, sx):
  if can_go(next[0], next[1]):
    que.append(next)

while que:
  current_y, current_x, current_d = que.popleft()
  for next in next_positions(current_y, current_x):
    if can_go(next[0], next[1]) and dist[next[0]][next[1]][next[2]] == inf:
      # print(next)
      if current_d == next[2]:
        dist[next[0]][next[1]][next[2]] = dist[current_y][current_x][current_d]
        que.appendleft(next)
      else:
        dist[next[0]][next[1]][next[2]] = dist[current_y][current_x][current_d] + 1
        que.append(next)

print(min(dist[gy][gx]))
