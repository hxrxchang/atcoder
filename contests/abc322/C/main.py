import bisect

N, M = map(int, input().split())
A = list(map(int, input().split()))

for i in range(1, N + 1):
  target = bisect.bisect_right(A, i)
  if target > 0 and A[target - 1] == i:
    print(0)
  else:
    print(A[target] - i)
