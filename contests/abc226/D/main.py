import math
from itertools import permutations

N = int(input())
towns = [list(map(int, input().split())) for _ in range(N)]

magics = set()

for p in permutations(towns, 2):
  t1 = p[0]
  t2 = p[1]
  x_diff = t1[0] - t2[0]
  y_diff = t1[1] - t2[1]
  g = math.gcd(x_diff, y_diff)
  magics.add((x_diff // g, y_diff // g))

print(len(magics))
