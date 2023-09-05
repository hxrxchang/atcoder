N, D = map(int, input().split())
walls = [list(map(int, input().split())) for _ in range(N)]
walls.sort(key=lambda x: x[1])

cnt = 1
last = walls[0][1]
for i in range(1, N):
  wall = walls[i]
  if wall[0] - last <= D - 1:
    continue
  else:
    cnt += 1
    last = wall[1]

print(cnt)
