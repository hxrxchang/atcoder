R, C = map(int, input().split())

board = []
bombs = []
for i in range(R):
  inp = input()
  board.append(list(inp))
  for j in range(C):
    if inp[j] != '.' and inp[j] != '#':
      bombs.append([i, j, int(inp[j])])
      board[i][j] = int(inp[j])

for i in range(R):
  for j in range(C):
    if board[i][j] == '#':
      for b in bombs:
        y, x, d = b[0], b[1], b[2]
        if abs(i - y) + abs(j - x) <= d:
          board[i][j] = '.'
    if isinstance(board[i][j], int):
      board[i][j] = '.'

for b in board:
  print("".join(b))
