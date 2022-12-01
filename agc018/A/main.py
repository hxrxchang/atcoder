import math

N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

if K > A[-1]:
  print("IMPOSSIBLE")
  exit()

gcd = 0
for i in range(N):
  gcd = math.gcd(gcd, A[i])

if K % gcd == 0:
  print("POSSIBLE")
else:
  print("IMPOSSIBLE")
