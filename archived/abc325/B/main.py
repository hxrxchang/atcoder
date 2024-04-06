N = int(input())
W = [tuple(map(int, input().split())) for _ in range(N)]

ans = 0
for i in range(0, 24):
  cnt = 0
  for w in W:
    if 9 <= (w[1] + i) % 24 and (w[1] + i) % 24 <= 17:
      cnt += w[0]
  ans = max(ans, cnt)

print(ans)
