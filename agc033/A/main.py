from collections import deque

H, W = map(int, input().split())
graph = [[0] * W for _ in range(H)]
que = deque()
black_cnt = 0

for i in range(H):
  s = input()
  for j in range(W):
    if s[j] == "#":
      graph[i][j] = 1
      que.append((i, j))
      black_cnt += 1

ans = 0
while black_cnt < H * W:
  next_que = deque()
  ans += 1
  while len(que) > 0:
    black_pos = que.popleft()
    y, x = black_pos[0], black_pos[1]
    for next_black_pos in [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]:
      y2, x2 = next_black_pos[0], next_black_pos[1]
      if 0 <= y2 and y2 < H and 0 <= x2 and x2 < W and graph[y2][x2] == 0:
        graph[y2][x2] = 1
        next_que.append((y2, x2))
        black_cnt += 1
  que = next_que

print(ans)

