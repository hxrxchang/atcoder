import math

N = int(input())

pairs = []

i = 1
while i <= math.sqrt(N):
  if N % i == 0:
    pairs.append((i, N // i))
  i += 1

ans = float('inf')
for pair in pairs:
  ans = min(ans, pair[0] - 1 + pair[1] - 1)

print(ans)
