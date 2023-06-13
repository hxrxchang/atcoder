H, W = map(int, input().split())
board = [list(input()) for _ in range(H)]

up = float('inf')
left = float('inf')
right = 0
down = 0

for h in range(H):
  for w in range(W):
    if board[h][w] == '#':
      up = min(up, h)
      down = max(up, h)
      left = min(left, w)
      right = max(right, w)

for h in range(up, down + 1):
  for w in range(left, right + 1):
    if board[h][w] == '.':
      print(h + 1, w + 1)
      break



