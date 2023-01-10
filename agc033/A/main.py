from collections import deque

H, W = map(int, input().split())
dist = [[-1] * W for _ in range(H)]
black_cnt = 0
que = deque()

for y in range(H):
  inp = list(input())
  for x in range(W):
    if inp[x] == "#":
      dist[y][x] = 0
      que.append((y, x))
      black_cnt += 1

cnt = 0
while black_cnt < H * W:
  cnt += 1
  next_que = deque()
  while que:
    black_pos = que.popleft()
    y, x = black_pos[0], black_pos[1]
    black_pos_dist = dist[y][x]
    for next_pos in [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]:
      y2, x2 = next_pos[0], next_pos[1]
      if 0 <= y2 and y2 < H and 0 <= x2 and x2 < W and dist[y2][x2] == -1:
        dist[y2][x2] = black_pos_dist + 1
        black_cnt += 1
        next_que.append((y2, x2))
  # que を入れ替えることで、このn回目の操作で新たに黒に変わったマスを記録できる
  que = next_que

print(cnt)

