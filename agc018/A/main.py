N, K = map(int, input().split())

A = list(map(int, input().split()))
A.sort()

def GCD(x, y):
  if y == 0:
    return x
  return GCD(y, x%y)

max = A[-1]
g = 0
for i in range(N):
  g = GCD(g, A[i])

if K <= max and K % g == 0:
  print("POSSIBLE")
else:
  print("IMPOSSIBLE")

