from itertools import permutations
from math import sqrt

N = int(input())
towns = [list(map(int, input().split())) for _ in range(N)]

perms = permutations(range(N))

cnt = 0
cnt2 = 0
for perm in perms:
  tmp = 0
  cnt2 += 1
  prev = towns[perm[0]]
  for i in range(1, N):
    current = towns[perm[i]]
    tmp += sqrt((prev[0] - current[0]) ** 2 + (prev[1] - current[1]) ** 2)
  cnt += tmp

ans = cnt / cnt2
print(ans)
