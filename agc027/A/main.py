N, X = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

cnt = 0

for i, a in enumerate(A):
  X -= a
  if i == N - 1 and X != 0:
    break
  elif X >= 0:
    cnt += 1

print(cnt)
