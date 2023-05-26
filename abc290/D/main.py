import math

T = int(input())

for t in range(T):
  N, D, K = map(int, input().split())
  period = N // math.gcd(N, D)
  count = (K - 1) // period
  print((D * (K - 1) + count) % N)
