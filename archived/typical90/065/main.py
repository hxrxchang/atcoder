from itertools import combinations

R, G, B, K = map(int, input().split())
X, Y, Z = map(int, input().split())

balls = ['R'] * R + ['G'] * G + ['B'] * B

cnt = 0
for c in combinations(balls, K):
  cnt_r = c.count('R')
  cnt_g = c.count('G')
  cnt_b = c.count('B')
  if cnt_r + cnt_g <= X and cnt_g + cnt_b <= Y and cnt_b + cnt_r <= Z:
    cnt += 1

print(cnt)
