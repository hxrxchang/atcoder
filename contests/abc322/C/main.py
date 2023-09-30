import bisect

N, M = map(int, input().split())
A = list(map(int, input().split()))
set_A = set(A)

for i in range(1, N + 1):
  if i in set_A:
    print(0)
  else:
    print(A[bisect.bisect_left(A, i)] - i)
