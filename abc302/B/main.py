from collections import deque

H, W = map(int, input().split())

board = [list(input()) for i in range(H)]

ans = []

def next_items(i, j):
  return [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1), (i, j - 1), (i, j + 1), (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)]

def check(x, y, z):
  return 0 <= x[0] < H and 0 <= x[1] < W and 0 <= y[0] < H and 0 <= y[1] < W and 0 <= z[0] < H and 0 <= z[1] < W

def check2(x, y, z):
  return board[x[0]][x[1]] == 'u' and board[y[0]][y[1]] == 'k' and board[z[0]][z[1]] == 'e'

for i in range(H):
  for j in range(W):
    start = board[i][j]
    if start != 's':
      ans = [(i, j)]
      continue
    for k, next_item in enumerate(next_items(i, j)):
      if 0 <= next_item[0] < H and 0 <= next_item[1] < W:
        if board[next_item[0]][next_item[1]] == 'n':
          if k == 0:
            x, y, z = (next_item[0] - 1, next_item[1] - 1), (next_item[0] - 2, next_item[1] - 2), (next_item[0] - 3, next_item[1] - 3)
          elif k == 1:
            x, y, z = (next_item[0] - 1, next_item[1]), (next_item[0] - 2, next_item[1]), (next_item[0] - 3, next_item[1])
          elif k == 2:
            x, y, z = (next_item[0] - 1, next_item[1] + 1), (next_item[0] - 2, next_item[1] + 2), (next_item[0] - 3, next_item[1] + 3)
          elif k == 3:
            x, y, z = (next_item[0], next_item[1] -1), (next_item[0], next_item[1] - 2), (next_item[0], next_item[1] - 3)
          elif k == 4:
            x, y, z = (next_item[0], next_item[1] + 1), (next_item[0], next_item[1] + 2), (next_item[0], next_item[1] + 3)
          elif k == 5:
            x, y, z = (next_item[0] + 1, next_item[1] -1), (next_item[0] + 2, next_item[1] - 2), (next_item[0] + 3, next_item[1] - 3)
          elif k == 6:
            x, y, z = (next_item[0] + 1, next_item[1]), (next_item[0] + 2, next_item[1]), (next_item[0] + 3, next_item[1])
          elif k == 7:
            x, y, z = (next_item[0] + 1, next_item[1] + 1), (next_item[0] + 2, next_item[1] + 2), (next_item[0] + 3, next_item[1] + 3)
          if check(x, y, z) and check2(x, y, z):
            print(i + 1, j + 1)
            print(next_item[0] + 1, next_item[1] + 1)
            print(x[0] + 1, x[1] + 1)
            print(y[0] + 1, y[1] + 1)
            print(z[0] + 1, z[1] + 1)


