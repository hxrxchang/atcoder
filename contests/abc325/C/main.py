from collections import deque

H, W = map(int, input().split())
grid = [list(input()) for _ in range(H)]

def candidates(y, x):
  return [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1), (y - 1, x - 1), (y + 1, x - 1), (y - 1, x + 1), (y + 1, x + 1)]

que = deque()
for y in range(H):
  for x in range(W):
    if grid[y][x] == "#":
      que.append((y, x))

visited = [[False] * W for _ in range(H)]
visited_set = set()
cnt = 0
while que:
  y, x = que.popleft()
  if (y, x) in visited_set:
    continue
  visited[y][x] = True
  visited_set.add((y, x))
  que2 = deque()
  for y2, x2 in candidates(y, x):
    if 0 <= y2 < H and 0 <= x2 < W and grid[y2][x2] == "#" and visited[y2][x2] == False:
      que2.append((y2, x2))
      visited[y2][x2] = True
      visited_set.add((y2, x2))
  while que2:
    y2, x2 = que2.pop()
    visited[y2][x2] = True
    visited_set.add((y2, x2))
    que.remove((y2, x2))
    for y3, x3 in candidates(y2, x2):
      if 0 <= y3 < H and 0 <= x3 < W and grid[y3][x3] == "#" and visited[y3][x3] == False:
        que2.append((y3, x3))
        visited[y3][x3] = True
  cnt += 1

print(cnt)
