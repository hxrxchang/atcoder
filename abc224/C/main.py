from itertools import combinations

N = int(input())
vertexes = [list(map(int, input().split())) for _ in range(N)]

cs = combinations(vertexes, 3)

cnt = 0
for c in cs:
  x1, x2, x3 = c[0][0], c[1][0], c[2][0]
  y1, y2, y3 = c[0][1], c[1][1], c[2][1]
  if (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1) != 0:
    cnt += 1

print(cnt)
