from collections import defaultdict

N = int(input())
max_n = 1001
board = [[0 for _ in range(max_n)] for _ in range(max_n)]


for _ in range(N):
    left_down_x, left_down_y, right_up_x, right_up_y = map(int, input().split())
    left_up_x, left_up_y = left_down_x, right_up_y
    right_down_x, right_down_y = right_up_x, left_down_y

    board[left_up_y][left_up_x] += 1
    board[right_down_y][right_down_x] += 1
    board[left_down_y][left_down_x] -= 1
    board[right_up_y][right_up_x] -= 1

# 縦方向の累積和
board_sum = [[0 for _ in range(max_n)] for _ in range(max_n)]
for i in range(max_n):
    board_sum[i][0] = board[i][0]

for i in range(max_n):
    for j in range(1, max_n):
        board_sum[i][j] = board_sum[i][j - 1] + board[i][j]

# 横方向の累積和と、その値の個数をカウント
cnt = defaultdict(int)
board_sum_2 = [[0 for _ in range(max_n)] for _ in range(max_n)]
board_sum_2[-1] = board_sum[-1]
for b in board_sum_2[-1]:
    cnt[b] += 1

for i in range(max_n - 2, -1, -1):
    for j in range(max_n - 1, -1, -1):
        board_sum_2[i][j] = board_sum_2[i + 1][j] + board_sum[i][j]
        cnt[board_sum_2[i][j]] += 1

for i in range(1, N + 1):
    print(cnt[i])
