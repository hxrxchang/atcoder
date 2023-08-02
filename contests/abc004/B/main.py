board = [list(input()) for _ in range(4)]

for i in range(3, -1, -1):
    tmp = ''
    for b in reversed(board[i]):
        tmp += b
    print(tmp)
