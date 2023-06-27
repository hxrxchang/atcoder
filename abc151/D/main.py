from collections import deque
from itertools import chain

H, W = map(int, input().split())
grid = [list(input()) for _ in range(H)]

def bfs(start_y, start_x):
  q = deque()
  dist = [[-1] * W for _ in range(H)]
  q.append((start_y, start_x))
  dist[start_y][start_x] = 0

  while q:
    current = q.popleft()
    y, x = current[0], current[1]
    for next_y, next_x in [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]:
      if 0 <= next_y < H and 0 <= next_x < W and grid[next_y][next_x] == '.' and dist[next_y][next_x] == -1:
        q.append((next_y, next_x))
        dist[next_y][next_x] = dist[y][x] + 1

  return max(chain.from_iterable(dist))


ans = 0
for i in range(H):
  for j in range(W):
    if grid[i][j] == '.':
      ans = max(ans, bfs(i, j))

print(ans)
