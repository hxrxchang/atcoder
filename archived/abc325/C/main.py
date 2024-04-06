from collections import deque

H, W = map(int, input().split())
grid = [list(input()) for _ in range(H)]

def candidates(y, x):
  return [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1), (y - 1, x - 1), (y + 1, x - 1), (y - 1, x + 1), (y + 1, x + 1)]

used = [[False] * W for _ in range(H)]

ans = 0
for y in range(H):
  for x in range(W):
    if grid[y][x] == '.' or used[y][x]:
      continue
    que = deque()
    que.append((y, x))
    while que:
      y2, x2 = que.pop()
      used[y2][x2] = True
      for y3, x3 in candidates(y2, x2):
        if 0 <= y3 < H and 0 <= x3 < W and grid[y3][x3] == '#' and not used[y3][x3]:
          que.append((y3, x3))
    ans += 1

print(ans)
