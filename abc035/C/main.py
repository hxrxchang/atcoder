N, Q = map(int, input().split())
board = [0] * N

for _ in range(Q):
    l, r = map(int, input().split())
    board[l-1] += 1
    if r < N:
        board[r] -= 1

board_sum = [0] * N
board_sum[0] = board[0] % 2
result = []
result.append(str(board_sum[0] % 2))
for i in range(1, N):
    board_sum[i] = board_sum[i-1] + board[i]
    result.append(str(board_sum[i] % 2))

print(''.join(result))

