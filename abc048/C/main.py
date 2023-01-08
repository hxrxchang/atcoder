N, x = map(int, input().split())
A = list(map(int, input().split()))

cnt = 0

if A[0] > x:
  cnt += A[0] - x
  A[0] = x

for i in range(N - 1):
  if A[i] + A[i + 1] > x:
    cnt += A[i] + A[i + 1] - x
    A[i + 1] = x - A[i]

print(cnt)
