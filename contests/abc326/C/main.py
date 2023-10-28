from collections import defaultdict

N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

data = [0] * ((10 ** 9) + 1)

for a in A:
  data[a] += 1

ans = 0

