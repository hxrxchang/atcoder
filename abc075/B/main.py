H, W = map(int, input().split())
board = [list(input()) for _ in range(H)]

for i in range(H):
    for j in range(W):
        if board[i][j] == '.':
            cnt = 0
            for target in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1), (i - 1, j - 1), (i - 1, j + 1), (i + 1, j + 1), (i + 1, j - 1)]:
                if 0 <= target[0] < H and 0 <= target[1] < W:
                    if board[target[0]][target[1]] == '#':
                        cnt += 1
            board[i][j] = str(cnt)

for b in board:
    print(''.join(b))

