H, W, N = map(int, input().split())
T = input()
grid = [list(input()) for _ in range(H)]

cnt = 0

for h in range(H):
  for w in range(W):
    if grid[h][w] == '#':
      continue
    tmp = (h, w)
    all_ok = True
    for t in T:
      if t == 'L':
        tmp = (tmp[0], tmp[1] - 1)
      elif t == 'R':
        tmp = (tmp[0], tmp[1] + 1)
      elif t == 'U':
        tmp = (tmp[0] - 1, tmp[1])
      elif t == 'D':
        tmp = (tmp[0] + 1, tmp[1])
      if not (0 <= tmp[0] < H and 0 <= tmp[1] < W) or grid[tmp[0]][tmp[1]] == '#':
        all_ok = False
        break
    if all_ok:
      cnt += 1

print(cnt)
