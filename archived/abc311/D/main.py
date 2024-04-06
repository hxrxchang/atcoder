H, W = map(int, input().split())
S = [input() for _ in range(H)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

seen = [[False] * W for _ in range(H)]

def dfs(x, y):
  seen[x][y] = True
  for dir in range(4):
    x2, y2 = x, y
    while S[x2 + dx[dir]][y2 + dy[dir]] == '.':
      seen[x2][y2] = True
      x2 += dx[dir]
      y2 += dy[dir]
    if not seen[x2][y2]:
      dfs(x2, y2)

dfs(1, 1)

res = sum(row.count(True) for row in seen)
print(res)
